from django.shortcuts import render,redirect
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST) #creates an inst with POST data
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username') #cleaned_data gets it as py dict
            messages.success(request,f'Account Created sucessfully for {username}') #f= formatted string in py
            return redirect('blog-saatvik')
    else:
        form=UserRegisterForm() #creates a blank form
    return render(request,'users/register.html',{'form':form})
#to restrict back button after logout

@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username=u_form.cleaned_data.get('username')
            messages.success(request,f'Profile Updated sucessfully for {username}')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'users/profile.html',context)