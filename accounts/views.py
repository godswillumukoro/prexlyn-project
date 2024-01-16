from django.shortcuts import render, redirect
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        messages.error(request, 'Testing error message')
        return redirect('signup')
    else:
        return render(request, 'accounts/signup.html')


def signin(request):
    if request.method == 'POST':
        print("REG")
        return redirect('index')
    else:
        return render(request, 'accounts/signin.html')


def signout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
