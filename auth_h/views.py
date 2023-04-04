# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('success')
                else:
                    redirect('failure')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def failure(request):
    return render(request, 'failure.html')
