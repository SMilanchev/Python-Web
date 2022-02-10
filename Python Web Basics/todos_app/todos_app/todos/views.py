from django.shortcuts import render, redirect

# from todos_app.todos.forms import CreateTodoForm
# from todos_app.todos.models import Todo
# from todos_app.todos.models.models import Person
#
#
# def index(req):
#     context = {
#         'todos': Todo.objects.all(),
#         'form': CreateTodoForm(),
#     }
#     return render(req,'index.html', context)
#
#
# def create_todo(req):
#     form = CreateTodoForm(req.POST)
#
#     if form.is_valid():
#         text = form.cleaned_data['text']
#         description = form.cleaned_data['description']
#         todo = Todo(
#             text=text,
#             description=description,
#             # owner=owner,
#         )
#         todo.save()
#
#         return redirect('/')
#
#     context = {
#         'todos': Todo.objects.all(),
#         'form': form,
#     }
#     return render(req, 'index.html', context)
#
#
# def change_todo_state(req, pk):
#     todo = Todo.objects.get(pk=pk)
#     todo.state = not todo.state
#     todo.save()
#
#     return redirect('/')
from todos_app.todos.forms import TodoForm
from todos_app.todos.models import Todo


def index(req):
    context = {
        'todos': Todo.objects.all(),
    }
    return render(req, 'todos_app/index.html', context)


def create_todo(req):
    form = TodoForm(req.POST)

    if req.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(req, 'todos_app/create.html', context)


def show_form(req, form):
    context = {
        'form': form
    }

    return render(req, 'todos_app/edit.html', context)


def update_todo(req, pk):
    todo = Todo.objects.get(pk=pk)

    if req.method == 'GET':
        return show_form(req, TodoForm(initial=todo.__dict__))
    else:
        form = TodoForm(req.POST, instance=todo)

        if form.is_valid():
            form.save()
            return redirect('index')

        return show_form(req, form)


def delete_todo(req, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('/')
