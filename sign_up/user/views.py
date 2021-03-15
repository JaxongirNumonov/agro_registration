from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.admin.views.decorators import (
    staff_member_required as _staff_member_required,
)
from .forms import UserForm, User


def staff_member_required(f):
    return _staff_member_required(f, login_url="login")


def dashboard_login(request):
    form = UserForm(None)
    if request.POST:
        email = request.POST.get('login_email', '')
        password = request.POST.get('login_password', '')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'base.html', {'form': form})


def dashboard_register(request):
    form = UserForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            password = request.POST.get('password')
            auth_user = authenticate(request, username=email, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('index')
    return redirect('login', {"form": form})


@staff_member_required
def index(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('second')
    return render(request, 'index.html', {"form": form})


@staff_member_required
def second(request):
    result = User.objects.all()
    if request.GET:
        users = User.objects.all()
        result = []
        for user in users:
            if request.GET.get('search') in user.full_name:
                result.append(user)

    return render(request, 'second.html', {"filtered_users": result})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')
