from django.db import models

#models

class Users(models.Model):
    # song title
    name = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    email = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.email)


