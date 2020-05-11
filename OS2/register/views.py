from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from home import views as v1
from register.forms import RegisterForm

# Create your views here.


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return v1.index(request)
        else:
            form = RegisterForm()

    return render(request,'register/register.html',{'form': form})
