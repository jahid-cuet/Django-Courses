from django.shortcuts import render,redirect
from .forms import RegisterForm,ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from posts.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


# (1)This is Registration form

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



# (1)This is Login Section
# this is for function base view
def Login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name, password=user_pass)

            if user is not None:
                messages.success(request,'Your Logged in Successfull')
                login(request,user)
                return redirect('Profile')
            else:
                messages.warning(request,'Your information is incorrect')
                return redirect('Login')


    else:
        form=AuthenticationForm()
    return render(request,'Register.html',{"form":form,'type':'Login'})

# this is for class based view




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
    data=Post.objects.filter(author=request.user)
    return render(request,'Profile.html',{'data':data})


@login_required
def edit_profile(request):

    if request.method=='POST':
        profile_form=ChangeUserForm(request.POST,instance=request.user)
        if  profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Your Information Changed Successfully')
            redirect('edit_profile')
    else:
         profile_form=ChangeUserForm(instance=request.user)
    return render(request,'edit_profile.html',{"form": profile_form,'type':'Profile'})


def PassChange(request):

    if request.method=='POST':
            form=PasswordChangeForm(request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Password Updated Successfull')
                update_session_auth_hash(request, form.user)

                redirect('Profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'PassChange.html',{"form":form})




def Logout(request):
    logout(request)
    return redirect('Login')