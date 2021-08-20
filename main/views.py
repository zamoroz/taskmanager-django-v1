from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, logout
from main.forms import *

from . import models

# Create your views here.


def user_check(request):
    if not request.user.is_authenticated:
        return redirect('sign-in')
        
class index_view(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'title': 'Главная',
                'tasks': models.task.objects.filter(user=request.user)
            }
        return user_check(request) or render(request, 'main/index.html', context)


class task_view(View):
    def get(self, request):
        return user_check(request) or render(request, 'main/tasks.html', {'form': task_form()})

    def post(self, request):
        form = task_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: return render(request, 'main/tasks.html', {'form': task_form(data=request.POST)})


def edit_task(request, task_id):
    if request.method == 'POST':
        form = task_form(request.POST)
        if form.is_valid():
            task = models.task.objects.get(pk=task_id)
            task.title = form.cleaned_data['title']
            task.task = form.cleaned_data['task']
            task.status = form.cleaned_data['status']
            task.user = form.cleaned_data['user']
            task.save()
            return redirect('home')
    else:
        task = models.task.objects.get(pk=task_id)
        return render(request, 'main/tasks.html', {
            'form': task_form(data={
                'title': task.title,
                'task': task.task,
                'status': task.status,
                'user': task.user
            })})


def delete_task(request, task_id):
    task = models.task.objects.get(pk=task_id)
    if task:
        task.delete()
    return redirect('home')


def success_task(request, task_id):
    task = models.task.objects.get(pk=task_id)
    if task:
        task.status = models.task_status(id=2)
        task.save()
    return redirect('home')


def defeat_task(request, task_id):
    task = models.task.objects.get(pk=task_id)
    if task:
        task.status = models.task_status(id=3)
        task.save()
    return redirect('home')


class sign_up(View):
    def post(self, request):
        form = sign_up_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render (request, 'main/signup.html', {'form': form}) 

    def get(self, request):
        form = sign_up_form()
        return render (request, 'main/signup.html', {'form': form})


class sign_in(View):
    def post(self, request):
        form = sign_in_form(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render (request, 'main/signin.html', {'form': form}) 

    def get(self, request):
        form = sign_in_form()
        return render (request, 'main/signin.html', {'form': form}) 


def logout_user(request):
    logout(request)
    return redirect('sign-in')