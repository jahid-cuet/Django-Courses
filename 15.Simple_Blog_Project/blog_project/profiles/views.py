
from django.shortcuts import render,redirect
from . import forms
def Add_Profile(request):
    if request.method=='POST':
        profile_form= forms.ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('Add_Profile')
    else:
        profile_form= forms.ProfileForm()
    return render(request,'Add_Profile.html',{"form":profile_form})

# Create your views here.

