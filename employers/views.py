from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from jobs.models import Job
from .models import EmployerProfile
from .forms import EmployerProfileForm
from employers.models import EmployerProfile

@login_required
def employer_dashboard(request):
    
    profile, created = EmployerProfile.objects.get_or_create(
        user=request.user
    )

    jobs = Job.objects.filter(employer=request.user)
    total_jobs = jobs.count()
    active_jobs = jobs.filter(is_active=True).count()

    context = {
        'profile': profile,
        'jobs': jobs,
        'total_jobs': total_jobs,
        'active_jobs': active_jobs,
    }

    return render(request, 'employers/dashboard.html', context)


@login_required
def employer_profile_view(request):
    profile = get_object_or_404(EmployerProfile, user=request.user)
    return render(request, 'employers/profile.html', {'profile': profile})


@login_required
def employer_profile_edit(request):
    profile = get_object_or_404(EmployerProfile, user=request.user)

    if request.method == 'POST':
        form = EmployerProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )
        if form.is_valid():
            form.save()
            return redirect('employer-profile')
    else:
        form = EmployerProfileForm(instance=profile)

    return render(request, 'employers/edit_profile.html', {'form': form})
