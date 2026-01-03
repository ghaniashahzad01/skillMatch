from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jobs.models import Job


@login_required
def employer_dashboard(request):
    user = request.user

    
    jobs = Job.objects.filter(employer=user)

    total_jobs = jobs.count()
    active_jobs = jobs.filter(is_active=True).count()

    context = {
        'jobs': jobs,
        'total_jobs': total_jobs,
        'active_jobs': active_jobs,
    }

    return render(request, 'employers/dashboard.html', context)
