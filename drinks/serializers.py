from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    '''the goal is to use this serializer when returning the model through the api.'''
    class Meta: # metadata that describes the model
        model = Drink # specify the model
        fields = ['id', 'name', 'description'] # specify the fields