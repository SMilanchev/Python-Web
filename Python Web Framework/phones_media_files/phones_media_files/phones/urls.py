from django.urls import path

from phones_media_files.phones.views import index, create_phone

urlpatterns = [
    path('', index, name='list phones'),
    path('create/', create_phone, name='create phone'),
]