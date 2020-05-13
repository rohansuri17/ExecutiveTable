from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Users
from .serializers import UsersSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(name = "", email = ""):
        if name != "" and email != "":
            Users.objects.create(name = name, email = email)

    def setUp(self):
        # add test data
        self.create_user("testuser", "test@test.com")
        self.create_user("Rohan Suri", "rohansuri17@gmail.com")


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the Users/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("users-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Users.objects.all()
        serialized = UsersSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
