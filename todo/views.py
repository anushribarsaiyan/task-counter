from django.shortcuts import render,redirect
from .forms import *
from .models import List
from .forms import List_form,CreateUserForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def task(request):
    form = List_form()
    if request.method == "POST":
        form = List_form(request.POST)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'task.html', context)



def table(request):
    s = List.objects.all()
    print(s)
    context = {'s': s}
    return render(request, 'task table.html', context)


def new_task(request):
    s = List.objects.all()
    print(s)
    context = {'s': s}
    return render(request, 'ok.html', context)

def  deleteTask(request,pk):
    task = List.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
    context={'item':task}
    return render(request,'delete_task.html',context)


def register(request):
    form= CreateUserForm()

    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}

    return render(request,'register.html',context)
