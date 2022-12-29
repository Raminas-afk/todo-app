from django.shortcuts import render, redirect
from .models import Task
from .forms import CreateTaskForm
# Create your views here.

def homepage(request):
    form = CreateTaskForm()
    tasks = Task.objects.filter(done=False)
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'todo_app/homepage.html', {
        "tasks": tasks,
        "form": form
    })

def task_archive(request):
    if request.method == "GET":
        completed_tasks = Task.objects.filter(done=True)
        return render(request, 'todo_app/task_archive.html', {
            "tasks": completed_tasks
        })

def task_detail(request, task_id):
    if request.method == "GET":
        specific_task = Task.objects.get(pk=task_id)
        return render(request, 'todo_app/task_detail.html', {
            "task": specific_task
        })

def delete_task(request, task_id):
    if request.method == "POST":
        specific_task = Task.objects.get(pk=task_id)
        specific_task.delete()
        return redirect('homepage')

def complete_task(request, task_id):
    if request.method == "POST":
        specific_task = Task.objects.get(pk=task_id)
        if specific_task.done:
            specific_task.done = False
        else:
            specific_task.done = True
        specific_task.save()
        return redirect('homepage')

def edit_task(request, task_id):
    if request.method == "GET":
        specific_task = Task.objects.get(pk=task_id)
        form = CreateTaskForm(instance=specific_task)
        return render(request, "todo_app/edit_task.html", {
            "form": form,
            "task": specific_task

        })
    if request.method == "POST":
        specific_task = Task.objects.get(pk=task_id)
        specific_task.name = request.POST['name']
        specific_task.save()
        return redirect('homepage')

def new_task(request):
    if request.method == "GET":
        form = CreateTaskForm()
        return render(request, "todo_app/new_task.html",{
            "form": form
        })
    if request.method =="POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
        form = CreateTaskForm()
        return redirect('homepage')