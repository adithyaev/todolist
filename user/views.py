from django.shortcuts import render
from datetime import date

# Create your views here.
def master(request):
    return render(request,('user/master.html'))

def add_task(request):
    return render(request,('user/add_task.html'))

def view_task(request):
    return render(request,('user/view_task.html'))

def pending_task(request):
    return render(request,('user/pending_task.html'))

def task_history(request):
    return render(request,('user/task_history.html'))

def profile(request):
    return render(request,('user/profile.html'))

def change_pass(request):
    return render(request,('user/change_password.html'))

def logout(request):
    return render(request,('user/logout.html'))
