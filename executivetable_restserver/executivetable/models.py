from django.db import models

#models

class Startup(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
    	return self.name

    class Meta:
        indexes = [
           models.Index(fields=['id',]),
        ]


class StartupProfile(models.Model):

    description = models.TextField(blank = True)

    startup_id = models.OneToOneField(Startup, on_delete = models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        indexes = [
           models.Index(fields=['id',]),
           models.Index(fields=['startup_id',]),
        ]


class User(models.Model):

    first_name = models.CharField(max_length = 45)

    last_name = models.CharField(max_length = 45)

    email = models.EmailField(max_length = 255, unique = True)

    password_digest = models.CharField(max_length = 255)

    startup_id = models.ForeignKey(Startup, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    class Meta:
        indexes = [
           models.Index(fields=['id',]),
           models.Index(fields=['last_name', 'first_name',]),
           models.Index(fields=['startup_id',]),
           models.Index(fields=['startup_role_id',]),
        ]


class UserProfile(models.Model):

    description = models.TextField(blank = True)

    user_id = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        indexes = [
           models.Index(fields=['id',]),
           models.Index(fields=['user_id',]),
        ]


class StartupRole(models.Model):

    title = models.CharField(max_length = 45)

    description = models.TextField()

    is_startup_owner = models.BooleanField(default = False)

    user_id = models.OneToOneField(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        indexes = [
           models.Index(fields=['id',]),
           models.Index(fields=['user_id',]),
        ]


class Education(models.Model):

    institution = models.CharField(max_length = 255)

    education_level = models.CharField(max_length = 255, blank = True)

    major = models.CharField(max_length = 255, blank = True)

    start_date = models.DateField()

    end_date = models.DateField(null = True)

    user_profile_id = models.OneToOneField(UserProfile, on_delete = models.CASCADE)

    def __str__(self):
        return "{} in {}\n{}".format(self.education_level, self.major, self.institution)

    class Meta:
        indexes = [
           models.Index(fields=['id',]),
           models.Index(fields=['user_profile_id',]),
        ]


class WorkExperience(models.Model):

    company = models.CharField(max_length = 255)

    title = models.CharField(max_length = 45)

    description = models.TextField(blank = True)

    start_date = models.DateField()

    end_date = models.DateField(null = True)

    user_profile_id = models.OneToOneField(UserProfile, on_delete = models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.title, self.company)

    class Meta:
        indexes = [
           models.Index(fields=['id',]),
           models.Index(fields=['user_profile_id',]),
        ]


class Connection(models.Model):

    user1_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_1")

    user2_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_2")

    status = models.IntegerField()

    action_user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "action_user_id")

    class Meta:
        indexes = [
           models.Index(fields=['id',]),
           models.Index(fields=['user1_id',]),
           models.Index(fields=['user2_id',]),
        ]


class PrivateMessage(models.Model):

    message = models.TextField()

    connection_id = models.ForeignKey(Connection, null = True, on_delete = models.CASCADE)

    user_sender_id = models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name = "user_sender_id")

    user_receiver_id = models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name = "user_receiver_id")

    startup_sender_id = models.ForeignKey(Startup, null = True, on_delete = models.CASCADE, related_name = "startup_sender_id")

    startup_receiver_id = models.ForeignKey(Startup, null = True, on_delete = models.CASCADE, related_name = "startup_receiver_id")

    def __str__(self):
	    return self.message

    class Meta:
        indexes = [
           models.Index(fields=['id',]),
           models.Index(fields=['connection_id',]),
           models.Index(fields=['sender_id',]),
           models.Index(fields=['receiver_id',]),
        ]


class MessageBoard(models.Model):

    name = models.CharField(max_length=45)

    user_message_board_id = models.ManyToManyField(User)

    def __str__(self):
	    return self.name

    class Meta:
        indexes = [
           models.Index(fields=['id',]),
        ]