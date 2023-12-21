from django.shortcuts import redirect, render

from common.models import User

# Create your views here.
def register(request):
    msg = ''
    
    # check if the form is submitted
    if request.method == 'POST':
        # retrieve data sent from the form and store in a variable
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_phone = request.POST['contact']
        user_password = request.POST['password']
        
        
        # check if email already exists
        if User.objects.filter(email=user_email).exists():
            msg = 'email already exists'
            return render(request,'common/register.html', {"status" : msg })
        
        # crate a new user(an instance)
        user = User(
            name = user_name,
            email = user_email,
            mobile = user_phone,
            password = user_password 
        )
        
        # insert into table(in to database)
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
