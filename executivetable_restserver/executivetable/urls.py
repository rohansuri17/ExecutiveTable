from django.urls import path
from django.conf.urls import include,url
from .views import ListUsersView
from .views import ListUserProfileView
from .views import ListStartupView
from .views import ListStartupProfileView
from .views import ListStartupRoleView
from .views import ListEducationView
from .views import ListWorkExperienceView
from .views import ListConnectionView
from .views import ListPrivateMessageView
from .views import ListMessageBoardView
#from .views import ListInfoUsersView
from .views import InfoUsersView

from executivetable import views 
#from .views import ListStartupRolesView
from rest_framework import routers 

router = routers.DefaultRouter()                      # add this
router.register(r'user', views.InfoUsersView, 'userinformation')

urlpatterns = [
    path('executivetable/', include(router.urls)),
    path('executivetable/user', ListUsersView.as_view(), name="users-all"),
    path('executivetable/userprofiles-all', ListUserProfileView.as_view(), name="userprofiles-all"),
    path('executivetable/', ListStartupView.as_view(), name="startup-all"),
    path('executivetable/', ListStartupProfileView.as_view(), name="startupprofile-all"),
    path('executivetable/', ListStartupRoleView.as_view(), name="startuprole-all"),
    path('executivetable/', ListEducationView.as_view(), name="education-all"),
    path('executivetable/', ListWorkExperienceView.as_view(), name="startup-all"),
    path('executivetable/', ListConnectionView.as_view(), name="connection-all"),
    path('executivetable/', ListPrivateMessageView.as_view(), name="privatemessage-all"),
    path('executivetable/', ListMessageBoardView.as_view(), name="messageboard-all"),
  
]
