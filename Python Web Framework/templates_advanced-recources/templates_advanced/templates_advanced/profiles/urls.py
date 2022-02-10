from django.urls import path

import templates_advanced.profiles.signals
from templates_advanced.profiles.views import profile_details

urlpatterns = [
    path('details/', profile_details, name='profile details'),
]