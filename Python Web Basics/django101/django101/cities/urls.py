from django.urls import path
from django101.cities.views import index, list_phones, test_index, create_person, show_forms_demo

urlpatterns = [
    path('', index),
    path('test/', test_index),
    path('create-person/', create_person, name='create person'),
    path('phones/', list_phones),
    path('forms/', show_forms_demo),

]
