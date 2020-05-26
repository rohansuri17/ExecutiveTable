from rest_framework import serializers
from .models import *
#from .models import StartupRoles

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password", "startup_id")

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("Profile Description")


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = '__all__'

class StartupProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupProfile
        fields = ("Startup Description", "Startup ID")

class StartupRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupRole
        fields = ("Role Title","Startup Description","Owner", "User ID")

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ("Institution", "Education Level", "Major", "Start Date", "End Date", "User ID")

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ("Company Name", "Job Title", "Description", "Start Date", "End Date", "User ID")
class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ("User 1", "User 2", "Status", "Action User")

class PrivateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateMessage
        fields = ("Message", "Connection ID", "User Sender ID","User Receiver ID", "Startup Sender ID", "Startup Receiver ID" )

class MessageBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageBoard
        fields = ("Name", "User ID")




'''
class StartupRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupRoles
        fields = ("Role title", "Role Description", "StartupID")
'''