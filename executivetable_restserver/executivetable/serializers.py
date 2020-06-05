from rest_framework import serializers
from .models import *
#from .models import StartupRoles
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

class InfoUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoUsers
        fields = ("first_name", "last_name", "email")
'''
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password", "startup_id")
'''
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("Profile Description")


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = ("Startup name")

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