from django.db import models
from django import forms

#models

class Startup(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
    	return self.name


class StartupProfile(models.Model):

    description = models.TextField(blank = True)

    startup_id = models.OneToOneField(Startup, on_delete = models.CASCADE)

    def __str__(self):
        return self.description



class User(models.Model):

    first_name = models.CharField(max_length = 45)

    last_name = models.CharField(max_length = 45)

    email = models.EmailField(max_length = 255, unique = True)

    password = models.CharField(max_length = 255)

    startup_id = models.ForeignKey(Startup, blank = True, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name) 


class UserProfile(models.Model):

    description = models.TextField(blank = True)

    user_id = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.description




class StartupRole(models.Model):

    title = models.CharField(max_length = 45)

    description = models.TextField()

    is_startup_owner = models.BooleanField(default = False)

    user_id = models.OneToOneField(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title


class Education(models.Model):

    institution = models.CharField(max_length = 255)

    education_level = models.CharField(max_length = 255, blank = True)

    major = models.CharField(max_length = 255, blank = True)

    start_date = models.DateField()

    end_date = models.DateField(null = True)

    user_profile_id = models.OneToOneField(UserProfile, on_delete = models.CASCADE)

    def __str__(self):
        return "{} in {}\n{}".format(self.education_level, self.major, self.institution)



class WorkExperience(models.Model):

    company = models.CharField(max_length = 255)

    title = models.CharField(max_length = 45)

    description = models.TextField(blank = True)

    start_date = models.DateField()

    end_date = models.DateField(null = True)

    user_profile_id = models.OneToOneField(UserProfile, on_delete = models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.title, self.company)



class Connection(models.Model):

    user1_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_1")

    user2_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_2")

    status = models.IntegerField()

    action_user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "action_user_id")



class PrivateMessage(models.Model):

    message = models.TextField()

    connection_id = models.ForeignKey(Connection, blank = True, null = True, on_delete = models.CASCADE)

    user_sender_id = models.ForeignKey(User, blank = True, null = True, on_delete = models.CASCADE, related_name = "user_sender_id")

    user_receiver_id = models.ForeignKey(User, blank = True, null = True, on_delete = models.CASCADE, related_name = "user_receiver_id")

    startup_sender_id = models.ForeignKey(Startup, blank = True, null = True, on_delete = models.CASCADE, related_name = "startup_sender_id")

    startup_receiver_id = models.ForeignKey(Startup, blank = True, null = True, on_delete = models.CASCADE, related_name = "startup_receiver_id")

    def __str__(self):
	    return self.message


class MessageBoard(models.Model):

    name = models.CharField(max_length=45)

    user_message_board_id = models.ManyToManyField(User)

    def __str__(self):
	    return self.name
