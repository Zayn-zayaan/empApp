from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password: 

            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('home')
                
                return render(request, 'login.html')
            
            return render(request, 'login.html')
        
        return render(request, 'login.html')
    
    return render(request, 'login.html')



def signup(request):


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if password == confirm_password:
                user = User.objects.create_user(username=username)
                user.set_password(password)
                user.save()
                return render(request, 'login.html', context)
                
            else:
                pass

            
        
        return render(request, 'signup.html', context)
    

    return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

def manage_employees(request):
    if request.user.is_superuser:
        users = User.objects.filter(is_superuser=False)
        context = {'users': users}
        return render(request, 'manage_employees.html', context)
    return HttpResponse('Invalid Request')


def active(request, id):
    user = User.objects.get(id=id)

    if user.is_active:
       user.is_active = False
       user.save()
    else:
        user.is_active = True
        user.save()

    return redirect('manage_employees')

def delete_user(request, id):
    user = User.objects.get(id=id)

    user.delete()

    return redirect('manage_employees')

