from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import requests
from . import models

# Create your views here.
def demo(request):
    return render(request,"index.html")


def login(request):
    return render(request, "login.html")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, 'login.html')


def button(request):
    return render(request,"button.html")

def form(request):
    
    username=request.session['username']
    if request.method=='POST':
        name=request.POST['name']
        dob = request.POST['date']
        email= request.POST['email']
        # number = request.POST['number']
        user=User.objects.create_user(name=name,email=email,dob=dob)
        user.save()
    return render(request,"form.html",{username:username})


def index(request):
    return render(request,"index.html")


def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            cpassword = form.cleaned_data['cpassword']
            user=authenticate(username=username,password=password,cpassword=cpassword)
            login(request,user)
            messages.success(request,("Registration Success"))
            return redirect('/')
    else:
        form =  UserCreationForm()

    return render(request,"register.html",{'form':form})



def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
        usr = models.Uuser(name=user['name'], public_repos=user['public_repos']) # create new model instance
        usr.save() #seve to db
    return render(request, 'core/github.html', {'user': user})

def newUser(request):
    user={}
    if 'username' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        emptyvalues=True
       
        if username=='' or password=='' or cpassword=='':
            emptyvalues=False


        if password==cpassword:
            continuev=True
        
        if continuev and emptyvalues:
            usr = models.Registration(username=username, password=password)
            usr.save()
            return redirect('login1')
    return render(request, 'register.html',{'user': user})

def login1(request):
    if 'username' in request.POST:

        username = request.POST['username']
        password = request.POST['password']

        try:
            entry=models.Registration.objects.get(username=username)
            request.session['username']=username
            return render(request,'button.html')
        except models.Registration.DoesNotExist:
            return render(request,'login.html',{'user':'please login'})
    else:
        return render(request,'login.html',{'user':'please login'})


# def register(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password= request.POST['password']
#         cpassword = request.POST['cpassword']
#         if password==cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"username taken")
#                 return redirect('register')
#
#             else:
#
#                 user=User.objects.create_user(username=username,password=password)
#                 user.save();
#                 return redirect('login')
#             print("user created")
#         else:
#             messages.info(request,"password not matched")
#             return redirect('register')
#         return redirect('/')
#     return render(request,"register.html")

# def login(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('login')
#     return render(request, 'login.html')
