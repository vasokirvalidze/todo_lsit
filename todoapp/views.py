from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method =="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'tasks':tasks ,
        'form':form
        }
    return render(request,'index.html',context)

def edit(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method=='POST':
        form = TaskForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'form':form
        }
    return render(request,'edit.html',context)

def delete(request, id):
    item = Task.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    context ={
        'item':item
        }
    return render(request,'delete.html',context)

def details(request, id):
    task = Task.objects.get(id=id)
    item = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    context = {
        'item':item,
        'form':form
    }
    return render(request, 'details.html',context)