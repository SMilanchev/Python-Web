from django.urls import path

from templates_advanced.pythons_app.views import  IndexView, PythonCreateView

urlpatterns = [
    # path('', index, name="index"),
    path('', IndexView.as_view(), name="index"),
    # path('create/', create, name="create"),
    path('create/', PythonCreateView.as_view(), name="create"),
]
