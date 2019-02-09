from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login ,logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserForm,ProfileForm
# Create your views here.
def index(request):
    return render(request,'index.html',{})
def register(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        profileform = ProfileForm(request.POST)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            #user.set_password(user.password)
            #user.save()
            profile = profileform.save(commit=False)
            #profile.user=user
            if 'pic' in request.FILES:
                profile.pic = request.FILES['pic']
            profile.save()
        else:
            print(userform.errors,profileform.errors)
    else:
        userform = UserForm()
        profileform = ProfileForm()

    return render(request,'register.html',{'userform':userform ,'profileform':profileform})

def log_in_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse('invalid data')
    else:
        return render(request,'login.html')
@login_required
def log_out_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
