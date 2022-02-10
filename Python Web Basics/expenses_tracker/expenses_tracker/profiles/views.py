from django.shortcuts import render, redirect

from expenses_tracker.core.profile_utils import get_profile
from expenses_tracker.expenses.models import Expense
from expenses_tracker.profiles.forms import CreateProfileForm, EditProfileForm


def profile_info(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context=context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context=context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile info')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'profile-edit.html', context=context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        Expense.objects.all().delete()
        profile.delete()
        return redirect('home')
    return render(request, 'profile-delete.html')
