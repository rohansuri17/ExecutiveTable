from django.contrib import admin
from .models import Users
from .models import UserProfile
from .models import Startup
#from .models import StartupRoles
# Register your models here.

admin.site.register(Users)
admin.site.register(UserProfile)
admin.site.register(Startup)
#admin.site.register(StartupRoles)