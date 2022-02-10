
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('test_project.common.urls')),
    path('pets/', include('test_project.pets.urls')),
]
