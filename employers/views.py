from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def employer_dashboard(request):
    return render(request, 'employers/dashboard.html')
