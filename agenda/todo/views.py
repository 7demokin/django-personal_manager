from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.


def index(request):
    """
    Purpose: request
    """
    search = request.GET.get('search', '')
    todos = Todo.objects.filter(
        title__contains=search).order_by('-id')

    context = {
        'search': search,
        'todos': todos
    }
    return render(request,
                  'todo/index.html',
                  context)
# end def


def view(request, id):
    """
    Purpose: request
    """
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todo/detail.html', context)
# end def


def edit(request, id):
    """
    Purpose: request
    """
    todo = Todo.objects.get(pk=id)
    if (request.method == 'GET'):
        todo_form = TodoForm(instance=todo)
        context = {
            'todo_form': todo_form,
            'id': id
        }
        return render(request, 'todo/edit.html', context)
    elif (request.method == 'POST'):
        todo_form = TodoForm(request.POST, instance=todo)
        if todo_form.is_valid():
            todo_form.save()
        context = {
            'todo_form': todo_form,
            'id': id
        }
        messages.success(request, 'Todoo actualizado correctamente!')
        return render(request, 'todo/edit.html', context)
# end def


def create(request):
    """
    Purpose: request
    """
    if (request.method == 'GET'):
        todo_form = TodoForm()
        context = {
            'todo_form': todo_form,
        }
        return render(request, 'todo/create.html', context)
    elif (request.method == 'POST'):
        todo_form = TodoForm(request.POST)
        if not todo_form.is_valid():
            context = {
                'todo_form': todo_form,
            }
            return render(request, 'todo/create.html', context)
        todo_form.save()
        return redirect('todo')
# end def

def delete(request, id):
    """
    Purpose: request
    """
    todo = Todo.objects.get(pk=id)
    todo.delete()
    return redirect('todo')
# end def