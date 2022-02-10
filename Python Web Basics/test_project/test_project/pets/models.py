from django.core.validators import MaxValueValidator
from django.db import models


class Pet(models.Model):
    CAT_CHOICE = 'Cat'
    DOG_CHOICE = 'Dog'
    SQUIRREL_CHOICE = 'Squirrel'
    PET_CHOICE = (
        (CAT_CHOICE, 'Kotence'),
        (DOG_CHOICE, 'Kuchence'),
        (SQUIRREL_CHOICE, 'Katerichka'),
    )
    type = models.CharField(
        max_length=8,
        choices=PET_CHOICE,
    )
    name = models.CharField(
        max_length=20,
    )
    age = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(55),
        ],
    )
    description = models.TextField(

    )
    image_url = models.URLField(

    )


class Like(models.Model):
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
    )
