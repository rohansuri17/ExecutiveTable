from rest_framework import generics
from .models import Users
from .models import UserProfile
from .models import Startup
#from .models import StartupRoles
from .serializers import UsersSerializer
from .serializers import UserProfileSerializer
from .serializers import StartupSerializer
#from .serializers import StartupRolesSerializer


class ListUsersView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class ListUserProfileView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UsersSerializer

class ListStartupView(generics.ListAPIView):
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