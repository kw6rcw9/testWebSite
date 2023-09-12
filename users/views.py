from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'user {username} was successful registered')
            return redirect('home')


    else:
        form = UserRegisterForm()

    form = UserRegisterForm()
    return render(
        request, 
        'users/registration.html',
          {
              'title': 'Registration page',
              'form': form
          }
    )

@login_required
def profile(request):
    return render(request, 'users/profile.html')