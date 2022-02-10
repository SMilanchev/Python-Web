from django.urls import path

from test_project.pets.views import create_pet, edit_pet, pet_details, like_pet, delete_pet, comment_pet

urlpatterns = [
    path('create_pet/', create_pet, name='create pet'),
    path('pet_details/<int:pk>', pet_details, name='pet details'),
    path('edit_pet/<int:pk>', edit_pet, name='edit pet'),
    path('like_pet/<int:pk>', like_pet, name='like pet'),
    path('delete_pet/<int:pk>', delete_pet, name='delete pet'),
    path('comment_pet/<int:pk>', comment_pet, name='comment pet')
]
