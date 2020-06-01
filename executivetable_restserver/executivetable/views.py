from rest_framework import generics
from rest_framework.response import Response
from .models import *
from rest_framework import status
#from .models import StartupRoles

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
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
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def infousers_list(request):
    if request.method == 'GET':
        users = InfoUsers.objects.all()
        serializer = InfoUsersSerializer(users, many=True)
        return Response(serializer.data)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InfoUsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = InfoUsers.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 

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