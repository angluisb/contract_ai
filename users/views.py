from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import  UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html",{'form': form})

def home(request):
    if not request.user.is_authenticated:
        user = request.user
        context = {'user': user}
    else:
        user = "Unknown"
        context = {'user': user}
    return render(request,"users/home.html", context)

def logout_view(request):
        logout(request)
        messages.success(request, f'You have been logged out!')
        return redirect('login')


