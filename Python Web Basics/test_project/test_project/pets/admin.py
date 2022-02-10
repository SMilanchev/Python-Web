from django.contrib import admin

from test_project.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
