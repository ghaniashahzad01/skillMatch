from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import JobForm
from .models import Job
from employers.models import EmployerProfile
from django.contrib import messages


@login_required
def create_job(request):

    profile = EmployerProfile.objects.get(user=request.user)

    if not profile.is_complete():
        messages.warning(
            request,
            "Please complete your company profile before posting a job."
        )
        return redirect('employer-dashboard')

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            return redirect('employer-dashboard')
    else:
        form = JobForm()

    return render(request, 'jobs/create_job.html', {'form': form})

@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('employer-dashboard')
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/edit_job.html', {
        'form': form,
        'job': job
    })


@login_required
def toggle_job_status(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user)

    job.is_active = not job.is_active
    job.save()

    return redirect('employer-dashboard')


@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user)

    if request.method == 'POST':
        job.delete()
        return redirect('employer-dashboard')

    return render(request, 'jobs/delete_job_confirm.html', {
        'job': job
    })




