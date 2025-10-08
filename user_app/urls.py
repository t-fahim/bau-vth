from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.user_index, name="user_index"),
    path("reg/", views.user_registration, name="user_registration"),
    path("login/", views.user_login, name="user_login"),
    path("profile/", views.user_profile, name="user_profile"),  ####
    path("logout/", views.user_logout, name="user_logout"),
    path("appointment/", views.user_appointment, name="user_appointment"),
]
