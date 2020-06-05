from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import User
from .models import UserProfile
from .models import Startup
#from .serializers import UsersSerializer
from .serializers import UserProfileSerializer
from .serializers import StartupSerializer
# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(first_name = "", last_name = "", email = "",password=""):
        if first_name != "" and last_name !="" and email != "" and password !="":
            User.objects.create(first_name = first_name, last_name = last_name, email = email,password=password)

    def setUp(self):
        # add test data
        self.create_user("testuser", "test@test.com")
        self.create_user("Rohan Suri", "rohansuri17@gmail.com")


class GetAllDataTest(BaseViewTest):
    '''
    def test_get_all_users(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the Users/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("users-all")
        )
        # fetch the data from db
        expected = User.objects.all()
        serialized = UsersSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    '''
    def test_get_all_userprofiles(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the Users/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("userprofiles-all")
        )
        # fetch the data from db
        expected = UserProfile.objects.all()
        serialized = UserProfileSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    '''
    def test_get_all_startups(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the Users/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("startup-all")
        )
        # fetch the data from db
        expected = Startup.objects.all()
        serialized = StartupSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    '''
    





