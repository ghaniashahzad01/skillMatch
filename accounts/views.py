from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployerRegisterForm
from employers.models import EmployerProfile
from django.contrib.auth import authenticate, login, logout

def employer_register(request):

    if request.method == "POST":
        form = EmployerRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('employer-dashboard')

        else:
            print(form.errors)

    else:
        form = EmployerRegisterForm()

    return render(request, 'accounts/employer_register.html', {
        'form': form
    })



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

           
            if user.is_employer:
                return redirect('employer-dashboard')

            return redirect('home')

       
        return render(request, 'accounts/login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')