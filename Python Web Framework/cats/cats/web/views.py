from django import forms
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from cats.common.form_mixins import BootstrapFormViewMixin
from cats.web.models import Cat


def index(request):
    context = {
        'title': 'Hello form FBV',
    }
    return render(request, 'index.html', context)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hello form CBV',
        }


def show_cats(request):
    context = {
        'cats': Cat.objects.all(),
        'cats_title': 'Hello FBV Cats'
    }
    return render(request, 'cats-list.html', context)


# class CatForm(forms.ModelForm):
#     class Meta:
#         model = Cat
#         fields = '__all__'
#         widgets = {
#
#         }


class CatCreateView(BootstrapFormViewMixin, CreateView):
    model = Cat
    fields = '__all__'
    template_name = 'create-cat.html'
    success_url = reverse_lazy('show cats cbv')

    # form_class = CatForm



class ShowCatsListView(ListView):
    model = Cat
    template_name = 'cats-list.html'
    context_object_name = 'cats'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats_title'] = 'Hello CBV cats'
        return context
