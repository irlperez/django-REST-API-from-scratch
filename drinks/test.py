from django.test import TestCase
from drinks.models import Drink
import json


# call tests with: python3 manage.py test
# call specific test with: python3 manage.py test appName.tests.testClass

class URLTests(TestCase):
    def setUp(self):  # setup instances of objects
        Drink.objects.create(name='Soda', description='light')
        Drink.objects.create(name='Pop', description='dark')

    def test_homepage(self):  # test home page
        response = self.client.get('/')

        # method un unittest.class. this will form a test assertion
        # first argument is the response, second is the value it should equal
        self.assertEqual(response.status_code, 200)

    
        ### test drink list - GET, POST ###    
    def test_drink_list_get(self):

        response = self.client.get('/drinks/')

        output = [
            {
                'id': 1,
                'name': 'Soda',
                'description': 'light'
            },
            {
                'id': 2,
                'name': 'Pop',
                'description': 'dark'
            }
        ]

        self.assertEqual(response.json(), output)


    def test_drink_list_post(self):

        response = self.client.post('/drinks/', {'name': 'newSoda', 'description': 'newTaste'})

        output = {
                'id': 3,
                'name': 'newSoda',
                'description': 'newTaste'
            }

        self.assertEqual(response.json(), output)

    ### test drink detail - GET, PUT, DELETE ###
    def test_drink_detail_get(self):

        response = self.client.get('/drinks/2')

        output = {
                'id': 2,
                'name': 'Pop',
                'description': 'dark'
            }

        self.assertEqual(response.json(), output)
    
    def test_drink_detail_put(self):

        response = self.client.put('/drinks/2', {'name': 'Pop', 'description': 'darker'}, content_type='application/json') # had to specify the content type
        

        output = {
                'id': 2,
                'name': 'Pop',
                'description': 'darker'
            }

        self.assertEqual(response.json(), output)


    def test_drink_detail_delete(self):

        response = self.client.delete('/drinks/2')
        

        output = {
                'id': 2,
                'name': 'Pop',
                'description': 'darker'
            }

        self.assertEqual(response.status_code, 204)