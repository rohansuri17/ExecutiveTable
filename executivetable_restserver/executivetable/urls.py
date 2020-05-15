from django.urls import path
from .views import ListUsersView
from .views import ListUserProfileView
from .views import ListStartupView
#from .views import ListStartupRolesView


urlpatterns = [
    path('executivetable/', ListUsersView.as_view(), name="users-all"),
    path('executivetable/', ListUserProfileView.as_view(), name="userprofiles-all"),
    path('executivetable/', ListStartupView.as_view(), name="startup-all"),
    #path('executivetable/', ListStartupRolesView.as_view(), name="startuproles-all"),

]
