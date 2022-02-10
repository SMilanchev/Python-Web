from django.urls import path

from test_project.common.views import index

urlpatterns = [
    path('', index, name='landing page'),
]