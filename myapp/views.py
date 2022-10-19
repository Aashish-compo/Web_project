from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.core.checks import messages
from django.contrib import messages
from django.contrib.auth import get_user_model

from myapp.models import Contact
User = get_user_model()

# Create your views here.
def index(request):
    context = {}
    print("home")
    return render(request, 'index.html', context=context)

def login(request):
    if request.method=="POST":  
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/index')
        else:
            messages.info(request,'username or password is incorrect')
            return redirect('login')
    
    return render(request,'Login.html')

def signup(request):
    if request.method=="POST":
        email = request.POST['email']
        password1 = request.POST['password1']
        Password2 = request.POST['password2']

        if password1==Password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken') 
                return redirect('/')
            else:        
                user = User.objects.create_user(password=password1,email=email)
                user.save();
                print("User created")
        else:
            print('password not matching')
            messages.info(request,'Password are not matching') 
            return redirect('login')
        return redirect("/")
           
    
    return render(request, 'Login.html',) 

def contact(request):
    if request.method =="POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data =  Contact(full_name=full_name, email=email, subject=subject, message=message)
        data.save()

        
        return redirect("home")

    return render(request, 'contact.html')


def about(request):
        return render(request, 'about.html')