from django.shortcuts import render
from datetime import date
from user.models import Task

# Create your views here.
def master(request):
    return render(request,('user/master.html'))


def add_task(request):
    msg = ''
    if request.method == 'POST':
        print("entered add task view")
        task_name = request.POST['taskname']
        task_description = request.POST['description']
        added_date = date.today()
        
        # check if task already exists
        if Task.objects.filter(task = task_name).exists():
            msg ='task already exists'
            return render(request,'user/add_task.html',{"status": msg})
        
        # create a new task
        task = Task(
            task = task_name,
            description = task_description,
            date = added_date
            )
        
        # insert into the table
        task.save()
        print("inserted task to the table")
        msg = 'Add task successfully'
    
    return render(request,'user/add_task.html',{"status": msg})

def view_task(request):
    task_list = Task.objects.all()
    return render(request,'user/view_task.html',{"tasks": task_list})

def edit_task(request,id):
    msg =''
    current_task = Task.objects.get(id=id)
    if request.method == 'POST':
        e_task = request.POST['edited_task']
        e_description = request.POST['edited_description']
        e_completed_date = request.POST['completed_date']
        e_status = request.POST['edited_status']
        
        current_task = Task.objects.get(id=id)
        print(current_task)
        print(current_task.task)
        print(current_task.description)
        print(current_task.completed_date)
        current_task.task = e_task,
        current_task.description = e_description,
        current_task.completed_date = e_completed_date,
        current_task.status = e_status
        print(current_task)
        print(current_task.task)
        print(current_task.description)
        print(current_task.completed_date)
        current_task.save()
        msg ='your task has been updated successfully'
        
    
    return render(request,'user/edit_task.html',{'status':msg,'task':current_task})

def task_history(request):
    return render(request,('user/task_history.html'))

def profile(request):
    return render(request,('user/profile.html'))

def change_pass(request):
    return render(request,('user/change_password.html'))

def logout(request):
    return render(request,('user/logout.html'))
    