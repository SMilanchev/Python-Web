from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import PythonCreateForm
from .models import Python
from ..core.decorators import any_group_required


# def index(request):
#     user = request.user
#     pythons = Python.objects.all()
#     return render(request, 'index.html', {'pythons': pythons})
from ..core.mixins import AnyGroupRequiredMixin


class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'
    paginate_by = 5



# # @login_required(login_url=reverse_lazy('sign in'))
# @any_group_required(groups=['User'])
# def create(request):
#     if request.method == 'GET':
#         form = PythonCreateForm()
#         return render(request, 'create.html', {'form': form})
#     else:
#         form = PythonCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#         return render(request, 'create.html', {'form': form})


class PythonCreateView(AnyGroupRequiredMixin, CreateView):
    model = Python
    fields = '__all__'
    template_name = 'create.html'
    success_url = reverse_lazy('index')


