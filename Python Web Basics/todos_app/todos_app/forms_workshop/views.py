from django.shortcuts import render, redirect

# Create your views here.
from todos_app.forms_workshop.user_form import UserForm


def show_form_data(req):
    if req.method == 'POST':
        form = UserForm(req.POST)

        if form.is_valid():
            values = ['name', 'age', 'email', 'password', 'text']
            [print(value, form.cleaned_data[value]) for value in values]
        else:
            print(form.errors)

    else:
        context = {
            'form': UserForm(),
        }
        return render(req, 'forms_workshop/form.html', context=context)