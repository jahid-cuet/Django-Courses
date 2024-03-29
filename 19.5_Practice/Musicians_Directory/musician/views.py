
from .import forms
from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

def Add_Musician(request):
    if request.method=="POST":          #User Post Request dise
        add_musician=forms.MusicianForm(request.POST) #form er data gulu nilam
        if add_musician.is_valid():
            add_musician.save()
            return redirect('home')
    else:
         add_musician=forms.MusicianForm() 
    return render(request,'Add_Musician.html',{'form': add_musician})

def Register(request):
    if request.method=='POST':
        register_form=RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
           
            messages.success(request,'Your registration is Successfull')
            redirect('Register')
    else:
        register_form=RegisterForm()
    return render(request,'Register.html',{"form":register_form,'type':'Register'})


class UserLoginView(LoginView):
    template_name = 'Register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('Profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    

@login_required
def Profile(request):
    # data=Post.objects.filter(author=request.user)
    return render(request,'Profile.html')


def Logout(request):
    logout(request)
    return redirect('Login')