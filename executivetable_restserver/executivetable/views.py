from rest_framework import generics
from rest_framework.response import Response
from .models import *
from rest_framework import status
#from .serializers import UsersSerializer
from .serializers import UserProfileSerializer
from .serializers import StartupSerializer
from .serializers import StartupRoleSerializer
from .serializers import StartupProfileSerializer
from .serializers import EducationSerializer
from .serializers import WorkExperienceSerializer
from .serializers import ConnectionSerializer
from .serializers import PrivateMessageSerializer
from .serializers import MessageBoardSerializer
from .serializers import InfoUsersSerializer
#from .serializers import StartupRolesSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework.response import Response

from knox.models import AuthToken

from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
class InfoUsersView(viewsets.ModelViewSet):
    serializer_class = InfoUsersSerializer
    queryset = InfoUsers.objects.all()
 
'''
class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
'''
class ListUserProfileView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

class ListStartupView(APIView):
    def get(self, request):
        startups = Startup.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer_class = StartupSerializer(startups,many=True)
        return Response(serializer_class.data)
    
    def post(self, request):

        Startup = request.data.get('Startup')

        # Create an article from the above data
        serializer = StartupSerializer(data=Startup)
        if serializer.is_valid(raise_exception=True):
            startup_saved = serializer.save()
        return Response({"success": "Startup '{}' created successfully".format(startup_saved.name)})
    
class ListStartupProfileView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Startup.objects.all()
    serializer_class = UserSerializer

class ListStartupRoleView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Startup.objects.all()
    serializer_class = UserSerializer

class ListEducationView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Startup.objects.all()
    serializer_class = UserSerializer

class ListWorkExperienceView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Startup.objects.all()
    serializer_class = UserSerializer

class ListConnectionView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Startup.objects.all()
    serializer_class = UserSerializer

class ListPrivateMessageView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Startup.objects.all()
    serializer_class = UserSerializer

class ListMessageBoardView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Startup.objects.all()
    serializer_class = UserSerializer
'''
class ListStartupRolesView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = StartupRoles.objects.all()
    serializer_class = UsersSerializer
'''