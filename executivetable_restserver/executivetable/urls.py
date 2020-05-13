from django.urls import path
from .views import ListUsersView


urlpatterns = [
    path('executivetable/', ListUsersView.as_view(), name="users-all")
]