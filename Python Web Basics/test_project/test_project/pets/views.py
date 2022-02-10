from django.shortcuts import render, redirect

# Create your views here.
from test_project.common.forms import CommentForm, FilterPetChoiceForm
from test_project.common.models import Comment
from test_project.pets.forms import PetCreateForm
from test_project.pets.models import Pet, Like


def create_pet(request):
    if request.method == "POST":
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing page')
    else:
        form = PetCreateForm()
    context = {
        'form': form
    }
    return render(request, 'pets/create_pet.html', context=context)


def comment_pet(req, pk):
    form = CommentForm(req.POST)
    if form.is_valid():
        form.save()

    return redirect('pet details', pk)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    context = {
        'pet': pet,
        'comments': Comment.objects.all(),
        "comment_form": CommentForm(
            initial={
                'pet_pk': pk
            }
        ),
    }

    return render(request, 'pets/pet_details.html', context=context)


def like_pet(req, pk):
    pet = Pet.objects.get(pk=pk)

    like = Like(
        pet=pet
    )
    like.save()

    return redirect('pet details', pet.id)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == "POST":
        form = PetCreateForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('landing page')
    else:
        form = PetCreateForm(instance=pet)

    context = {
        'form': form
    }

    return render(request, 'pets/edit_pet.html', context=context)


def delete_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    if req.method == "POST":
        pet.delete()
        return redirect('landing page')

    context = {
        'pet': pet,
    }

    return render(req, 'pets/pet_delete.html', context)
