from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, ProfileForm
from .models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            profile = profile_form.save( commit=False )
            profile.user = user
            profile.save()
            messages.success(request, f'{username}"s  Account has been created!   !')
            return redirect('login')
    else:
        form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request,'users/register.html',{'form': form, 'profile_form':profile_form})


@login_required
def profile(request):
    return render(request, 'users/profile.html', )
