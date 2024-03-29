from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserBankAccount
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views import View
from django.shortcuts import redirect

class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')
    
    def form_valid(self,form):
        # print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        # print(user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
    

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

# class UserLogoutView(LogoutView):
#     def get_success_url(self):
#         if self.request.user.is_authenticated:
#             logout(self.request)
#         return reverse_lazy('home')
def user_logout(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render, redirect
from django.views import View
from .forms import UserUpdateForm

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

def Passchange(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('profile')
    