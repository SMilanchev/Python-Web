from django.http import HttpResponse
from django.shortcuts import render, redirect

from django101.cities.models import Person


def show_forms_demo(req):
    return render(req, 'forms_demo.html')


def index(req):
    context = {
        'name': 'Peshko',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)


def list_phones(req):
    context = {
        'phones': [
            {'name': 'Samsung S900',
                'quantity': 4},
            {'name': 'Xiaomi Redmi Note 9',
             'quantity': 3},
            {'name': 'iPhone 12',
             'quantity': 1}
        ],
    }

    # context['message'] = 'Phones list'
    return render(req, 'cities/phones.html', context)


def test_index(req):
    return HttpResponse('It works')


def create_person(req):
    Person(
        name='Peshkata',
        age=17,
        home_town='Vratza'
    ).save()

    return redirect('/cities')
