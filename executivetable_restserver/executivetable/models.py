from django.db import models

#models

class Startup(models.Model):
    # song title

    StartupID = models.AutoField(primary_key=True)

    startup_name = models.CharField(max_length=255, null=False, default = None)

    def __str__(self):
    	return "{} - {}".format(self.StartupID,self.startup_name)
'''
class StartupRoles(models.Model):
    # song title
	Role = models.AutoField(primary_key=True)
	role_title = models.CharField(max_length=255,null = False)
	role_description= models.TextField(default = "")
	StartupID = models.ForeignKey(Startup, on_delete=models.CASCADE, verbose_name="Related StartupID")

	def __str__(self):
		return "{} - {}".format(self.role_title,self.role_description, self.StartupID)
    	
'''
class Users(models.Model):
    # song title
    first_name = models.CharField(max_length=255, null=False, default = "")
    # name of artist or group/band
    last_name = models.CharField(max_length=255, null=False, default = "")
    email = models.EmailField(max_length=255, null=False, default = "")

    password = models.CharField(max_length=255, null = False, default = "")

    Startup = models.ForeignKey(Startup, on_delete=models.CASCADE, blank = True, null = True)

    #Role = models.ForeignKey(StartupRoles, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return "{} - {}".format(self.first_name, self.last_name, self.email, self.password, self.Startup)

class UserProfile(models.Model):
    # song title
    ProfileId = models.OneToOneField(Users,on_delete=models.CASCADE,primary_key=True, default = None)
    profile_description = models.TextField(default = "")

    def __str__(self):
        return "{} - {}".format(self.ProfileId, self.profile_description)

   






