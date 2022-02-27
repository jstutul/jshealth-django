from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import requests
import json
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

url = 'http://127.0.0.1:8000/api/api-services/'


def index(request):
    client_url = 'http://127.0.0.1:8000/api/api-clientsay/'
    services_list = requests.get(url).json()
    client_list = requests.get(client_url).json()
    context = {
        'services_list': services_list,
        'client_list': client_list,
    }
    return render(request, 'index.html', context)


def contactus(request):
    return render(request, 'contactus.html')


def services(request):
    services_list = requests.get(url).json()
    context = {
        'services_list': services_list,
    }
    return render(request, 'services.html', context)

@login_required(login_url='loginview')
def signleservice(request, id):
    services_list = requests.get(url + str(id)).json()
    print(services_list)
    context = {
        'single_service': services_list,
    }
    return render(request, 'singleservice.html', context)


def about(request):
    about_url = "http://127.0.0.1:8000/api/api-aboutus/"
    doctor_list = requests.get(about_url).json()
    context = {
        'doctor_list': doctor_list,
    }
    return render(request, 'about.html', context)


def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            user_name = request.POST.get('username')
            password = request.POST.get('password')
            next = request.GET.get("next", '')
            user = authenticate(request, username=user_name, password=password)
            if user is not None:
                login(request, user)
                if next != "":
                    return redirect(next)
                return redirect('home')
            else:
                messages.info(request, "Enter correct username and password", extra_tags="login_error")
                return redirect('loginview')
        else:
            return render(request, 'login.html')


@login_required(login_url='loginview')
def Logoutview(request):
    logout(request)
    return redirect('loginview')


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.info(request, "Register Successfull")
            return redirect('signup')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)
