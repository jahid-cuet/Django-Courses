from django.shortcuts import render,redirect
from .import forms 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.

def home(request):
    return render(request,'home.html')
def Signup(request):
    if not request.user.is_authenticated:

        if request.method=="POST":
            form=forms.RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'The Account created Successfully')
                # redirect('home')
        else:
            form=forms.RegisterForm()

        return render(request,'signup.html',{'form':form})
    else:
        return redirect('Profile')

def Login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                userpass=form.cleaned_data['password']
                user=authenticate(username=name,password=userpass)   #Cheack kortesi user Database e ase kina
                if user is not None:
                    login(request,user)
                    return redirect('Profile')
        else:
            form=AuthenticationForm()

        return render(request,'login.html',{'form':form})
    else:
        return redirect('Profile')

def Profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
        else:
            form = forms.ChangeUserData(instance=request.user)
        return render(request, 'Profile.html', {'form': form})
    else:
        return redirect('Signup')



def Logout(request):
    logout(request)
    return redirect('Login')



# With old Password
# def Passchange(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = PasswordChangeForm(user=request.user, data=request.POST)
#             if form.is_valid():
#                 form.save()
#                 # password update korbe
#                 update_session_auth_hash(request, form.user)
#                 return redirect('Profile')
#         else:
#             form = PasswordChangeForm(user=request.user)
#         return render(request, './passchange.html', {'form': form})
#     else:
#         return redirect('Login')
    
# without old password
def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect('Profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'passchange.html', {'form': form})
    else:
        return redirect('Login')


