from django.urls import path
from django.conf.urls import include,url
#from .views import ListUsersView
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
from knox.views import LogoutView

from .views import UserAPIView, RegisterAPIView, LoginAPIView

router = routers.DefaultRouter()                      # add this
router.register(r'user', views.InfoUsersView, 'userinformation')

urlpatterns = [
    path('executivetable/', include(router.urls)),
    # path('executivetable/user', ListUsersView.as_view(), name="users-all"),
    path('', include('knox.urls')),
    path('user', UserAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout'),
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
