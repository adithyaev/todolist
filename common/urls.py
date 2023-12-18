from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.login,name='login'),
   
]