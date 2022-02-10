from django import forms

from test_project.common.models import Comment
from test_project.pets.models import Pet


class CommentForm(forms.ModelForm):
    pet_pk = forms.CharField(
        widget=forms.HiddenInput(),
    )

    class Meta:
        model = Comment
        fields = ("comment", "pet_pk")

    def save(self, commit=True):
        pet_pk = self.cleaned_data['pet_pk']
        pet = Pet.objects.get(pk=pet_pk)
        comment = Comment(
            comment=self.cleaned_data['comment'],
            pet=pet,
        )

        if comment:
            comment.save()

        return comment


class FilterPetChoiceForm(forms.Form):
    PETS_CHOICES = (
        (None, 'Not defined'),
        ('Cat', 'Kotenca'),
        ('Dog', 'Kuchenca'),
        ('Squirrel', 'Katerichki'),
    )
    pet_chosen = forms.ChoiceField(
        choices=PETS_CHOICES,
        required=False,

    )
