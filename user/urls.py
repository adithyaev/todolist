from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('home/',views.master,name='master'),
    path('addtask/',views.add_task,name='addTask'),
    path('viewtask/',views.view_task,name='viewTask'),
    path('pending/',views.pending_task,name='pending'),
    path('history/',views.task_history,name='history'),
    path('change/',views.change_pass,name='change'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),
    
   
]