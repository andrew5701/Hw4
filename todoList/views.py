from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Todo


# Create your views here.

def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todoList/index.html', context)


def add(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'todoList/add.html', context)


def update(request, task_id):
    # update the product with product_id
    task = Todo.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=task)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')




    context = {'form': form, 'task': task}

    return render(request, 'todoList/update.html', context)


def delete(request, task_id):
    # delete the product with product_id
    task = Todo.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')

    context = {'task': task}
    return render(request, 'todoList/index.html', context)


def search(request):
    search_term = request.GET.get('searchbar' or '')
    tasks = Todo.objects.all().filter(task_name__contains=search_term)
    context = {'tasks': tasks}
    return render(request, 'todoList/index.html', context)


