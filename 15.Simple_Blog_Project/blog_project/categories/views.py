from django.shortcuts import render,redirect
from  .import forms
def Add_Categories(request):
    if request.method=='POST':        # User post request koreche
        category_form=forms.CategoryForm(request.POST) # user theke data gulu nilam
        if category_form.is_valid():  # data gula valid kina check korlam
            category_form.save()  # data jodi valid hoy tahole database e save korlam
            return redirect('Add_Categories') # sob thik thak thakle same url e pathai dilam
    else:
         category_form=forms.CategoryForm() # jodi post request na kora hoy tahole user blank page pabe 
    return render(request,'Add_Category.html',{'form': category_form})
# Create your views here.
