from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        # Get values from form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        # Check if password matches confirm password
        if password == confirm_password:
            # check email availability
            if User.objects.filter(username=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')
        else:
            # Push to DB
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=email, password=password)
            # Login after success
            user.save()
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
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
