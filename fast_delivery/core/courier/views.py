from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings

@login_required(login_url='/sign-in/?next=/courier/')
def home(request):
    return redirect(reverse('courier:available_jobs'))

@login_required(login_url='/sign-in/?next=/courier/')
def available_jobs_page(request):
    return render(request, 'courier/available_jobs.html', {
        "GOOGLE_API_KEY" : settings.GOOGLE_API_KEY
    })