from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = models.register(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
            password = password
        )
        user.save()
        return redirect('login')
    return render(request,'signup.html')

def login(request):
    error =""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        user = models.register.objects.filter(email=email, password=password).first()
        if user:
            #Login successful
            request.session['user_id'] = user.id
            return redirect('index')
        else:
            error = "invalid email or password"

    return render(request,"login.html",{"error":error})

def index(request):
    if not request.session.get('user_id'):
        return redirect('login')
    return render(request,"index.html")

def logout(request):
    request.session.flush()
    return redirect('login')
# Create your views here.
