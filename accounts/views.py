from django.shortcuts import render, redirect
from .forms import EmployerRegisterForm

def employer_register(request):
    form = EmployerRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'accounts/employer_register.html', {'form': form})
