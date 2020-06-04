from rest_framework import generics
from rest_framework.response import Response
from .models import *
from rest_framework import status
from .serializers import UsersSerializer
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

class InfoUsersView(viewsets.ModelViewSet):
    serializer_class = InfoUsersSerializer
    queryset = InfoUsers.objects.all()
 

class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class ListUserProfileView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UsersSerializer

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
    serializer_class = UsersSerializer

class ListStartupRoleView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Startup.objects.all()
    serializer_class = UsersSerializer

class ListEducationView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Startup.objects.all()
    serializer_class = UsersSerializer

class ListWorkExperienceView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Startup.objects.all()
    serializer_class = UsersSerializer

class ListConnectionView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Startup.objects.all()
    serializer_class = UsersSerializer

class ListPrivateMessageView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Startup.objects.all()
    serializer_class = UsersSerializer

class ListMessageBoardView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Startup.objects.all()
    serializer_class = UsersSerializer
'''
class ListStartupRolesView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = StartupRoles.objects.all()
    serializer_class = UsersSerializer
'''