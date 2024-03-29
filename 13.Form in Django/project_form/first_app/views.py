from django.shortcuts import render
from . forms import contactForm, StudentData, PasswordValidationProject

def form(request):
   
    return render(request,'form.html')


def about(request):
    if request.method =='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        return render(request,'about.html', {'email':email,'password':password})
    else:
         return render(request,'about.html')
    




# def DjangoForm(request):
#     if request.method=='POST':
#         form = contactForm(request.POST,request.FILES)
#         if form.is_valid():
#             file=form.cleaned_data['file']
#             with open('./first_app/upload/'+ file.name,'wb+') as destination:
#                 for chunk in file.chunks():
#                     destination.write(chunk)
#             print(form.cleaned_data)
#             return render(request,'django_form.html',{'form':form})

#     else:
#         form = contactForm()
#     return render(request,'django_form.html',{'form':form})



def StudentForm(request):
    if request.method=='POST':
        form = StudentData(request.POST,request.FILES)
        if form.is_valid():

            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request,'django_form.html',{'form':form})


def PasswordValidation(request):
    if request.method == 'POST':
        form = PasswordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationProject()
    return render(request, 'django_form.html', {'form':form})    