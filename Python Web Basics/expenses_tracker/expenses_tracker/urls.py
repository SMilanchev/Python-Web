from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expenses_tracker.expenses.urls')),
    path('profiles/', include('expenses_tracker.profiles.urls')),
]
