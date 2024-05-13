from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from core.customer import forms

@login_required()
def home(request):
    return redirect(reverse('customer:profile'))

@login_required(login_url='/sign-in/?next=/customer/')
def profile_page(request):
    user_form = forms.BasicUserForm()

    return render(request, 'customer/profile.html', {
        'user_form': user_form,
    })  
    

