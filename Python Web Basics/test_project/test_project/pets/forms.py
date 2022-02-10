from django import forms

from test_project.core.forms import BootstrapFormMixin
from test_project.pets.models import Pet


class PetCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
