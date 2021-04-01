from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from . import models
from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def fun(request):
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            user_login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def signup(request):
    if request.method == "GET":
        form = CreateUserForm()
        context = {"form": form}
        return render(request, 'signup.html', context=context)

    else:
        form = CreateUserForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            if user is not None:
                return redirect('login')

        else:
            return render(request, 'signup.html', context=context)


def signout(request):
    logout(request)
    return redirect('home')

def index(request):
    return render(request,'index.html')

def chat(request):
    return render(request, 'chatroom.html')

def games(request):
    return render(request, 'games.html')

def q1(request):
    return render(request, 'q1.html')

def q1w(request):
    return render(request, 'q1w.html')

def q1r(request):
    return render(request, 'q1r.html')

def q2(request):
    return render(request, 'q2.html')

def q2w(request):
    return render(request, 'q2w.html')

def q2r(request):
    return render(request, 'q2r.html')

def q3(request):
    return render(request, 'q3.html')

def q3w(request):
    return render(request, 'q3w.html')

def q3r(request):
    return render(request, 'q3r.html')

def q4(request):
    return render(request, 'q4.html')

def q4w(request):
    return render(request, 'q4w.html')

def q4r(request):
    return render(request, 'q4r.html')

def q5(request):
    return render(request, 'q5.html')

def q5w(request):
    return render(request, 'q5w.html')

def q5r(request):
    return render(request, 'q5r.html')

def end(request):
    return render(request, 'end.html')