from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        Contact = authenticate(username=username, password=password)
        if Contact is not None:
            login(request,Contact)
            return redirect("/")
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(username=username,password=password,email=email,phone=phone)
        contact.save()
        messages.success(request, 'Your data has been stored!')
    return render(request,'signup.html')