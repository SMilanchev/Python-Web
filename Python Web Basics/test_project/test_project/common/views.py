from django.shortcuts import render

from test_project.common.forms import FilterPetChoiceForm
from test_project.pets.models import Pet


def index(req):
    filter_form = FilterPetChoiceForm(req.GET)
    filter_form.is_valid()
    pet_chosen = filter_form.cleaned_data['pet_chosen']
    Pet.objects.all()
    if pet_chosen == 'Cat':
        pets_to_show = Pet.objects.filter(type='Cat')
    elif pet_chosen == 'Dog':
        pets_to_show = Pet.objects.filter(type='Dog')
    elif pet_chosen == 'Squirrel':
        pets_to_show = Pet.objects.filter(type='Squirrel')
    else:
        pets_to_show = Pet.objects.all()

    context = {
        # 'showed_pets': pets_to_show,
        'pets': pets_to_show,
        'pet_filter': filter_form,
    }

    return render(req, 'landing_page.html', context=context)