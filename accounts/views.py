from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('txt')
        email = request.POST.get('registration_email')
        password = request.POST.get('registration_pswd')
        print(username,email,password)
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken!')
            return redirect('login')
        else:
            user = User.objects.create_user(username = username,email = email,password = password)
            user.save()
            return redirect('login')

    else:
        return render (request,"log in.html")    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pswd')
        print(username,password)
        user = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            print("User logged in successfully")
            return redirect('/')
        else:
            messages.info(request,'Email or password is incorrect!')
            return redirect('login')
    else:
        return render (request,"log in.html")

def logout(request):
    auth.logout(request)
    return redirect('login')
