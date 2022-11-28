from django.http import JsonResponse # returns json responses
from .models import Drink # gets drink model
from .serializers import DrinkSerializer # returns serializers
from rest_framework.decorators import api_view # decorator
from rest_framework.response import Response # response object
from rest_framework import status # status codes

@api_view(['GET'])
def homepage(request):
    
    return Response('homepage',status=status.HTTP_200_OK)

@api_view(['GET', 'POST']) # using the decorator we can condition the request. Get data. POST (create)
def drink_list(request, format=None):

    if request.method == 'GET':
        # get all the drinks
        drinks = Drink.objects.all() # access the drink class. the objects. list of drinks

        # serialize them
        serializer = DrinkSerializer(drinks, many=True) # first argument is the drink list. the second is saying to do all objects.

        # return JsonResponse
        # return JsonResponse({'drinks' : serializer.data}) # keeping the old version
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST': # checks for the method to be POST
        serializer = DrinkSerializer(data=request.data) # take data from request
        if serializer.is_valid(): # us a method to check if data is valid
            serializer.save() # saves the data
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE']) # GET information, PUT (update), DELETE
def drink_detail(request, id, format=None):
    # start testing the request methods

    # checks if it's a valid request
    try:
        drink = Drink.objects.get(pk=id) # calling a method built in our models. objects function. get method(passing through primary key)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

        

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data) # this isn't JSON specific like JsonResponse. So we get a front end. No login required.
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data) # given the drink. get the data from the request
        if serializer.is_valid(): # check if it's valid
            serializer.save() # save if so
            return Response(serializer.data) # return that data 
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST) # else return error, with status code
    elif request.method == 'DELETE':
        drink.delete() # delete the data
        return Response(status=status.HTTP_204_NO_CONTENT)
    
