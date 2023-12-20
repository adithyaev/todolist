from django.shortcuts import redirect, render

from common.models import User

# Create your views here.
def register(request):
    msg = ''
    if request.method == 'POST':
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_phone = request.POST['contact']
        user_password = request.POST['password']
        
        if User.objects.filter(email=user_email).exists():
            msg = 'email already exists'
            return render(request,'common/register.html', {"status" : msg })
        
        user = User(
            name = user_name,
            email = user_email,
            mobile = user_phone,
            password = user_password 
        )
        user.save()
        msg = 'user registered successfully'
    return render(request,'common/register.html', {"status" : msg })

def login(request):
    msg = ''
    new_user = User.objects.all()
    
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        try:
            user = User.objects.get(email = user_name,password = password)
            return redirect('user:master')
        except:
            msg = 'invalid user name or password'
    
    return render(request,'common/login.html',{"status": msg,"user": new_user})
