from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.staff_index, name="staff_index"),
    path("profile/", views.staff_profile, name="staff_profile"),
    path("prescription/", views.staff_prescription, name="staff_prescription"),
    path("appointment/", views.staff_all_appointment, name="staff_all_appointment"),
    path("logout/", views.staff_logout, name="staff_logout"),
    path("message/", views.staff_message, name="staff_message"),
    path(
        "appointment/details/<int:id>",
        views.staff_appointment_details,
        name="staff_details",
    ),
    path("sample/<int:id>", views.staff_sample, name="sample"),
]
