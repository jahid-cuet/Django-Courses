from django.shortcuts import render,redirect
from .import forms

def Add_Musician(request):
    if request.method=="POST":          #User Post Request dise
        add_musician=forms.MusicianForm(request.POST) #form er data gulu nilam
        if add_musician.is_valid():
            add_musician.save()
            return redirect('home')
    else:
         add_musician=forms.MusicianForm() 
    return render(request,'Add_Musician.html',{'form': add_musician})
