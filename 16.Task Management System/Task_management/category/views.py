
from django.shortcuts import render,redirect
from  .import forms
from  .import models
def Add_Category(request):
    if request.method=='POST':                   # User post request koreche
        category_form=forms.CategoryForm(request.POST)   # user theke data gulu nilam
        if  category_form.is_valid():                # data gula valid kina check korlam
            category_form.save()                     # data jodi valid hoy tahole database e save korlam
            return redirect('Add_Category')          # sob thik thak thakle same url e pathai dilam
    else:
            category_form=forms.CategoryForm()           # jodi post request na kora hoy tahole user blank page pabe 
    return render(request,'Add_Category.html',{'form':  category_form})




# def edit_task(request,id):
#     task=models.TaskCategory.objects.get(pk=id)
#     task_form=forms.CategoryForm(instance=task)
#     if request.method=='POST':                               # User post request koreche
#         task_form=forms.CategoryForm(request.POST,instance=task)               # user theke data gulu nilam
#         if  task_form.is_valid():                            # data gula valid kina check korlam
#             task_form.save()                                 # data jodi valid hoy tahole database e save korlam
#             return redirect('home')                      # sob thik thak thakle same url e pathai dilam
#                         # jodi post request na kora hoy tahole user blank page pabe 
#     return render(request,'Add_Category.html',{'form': task_form})


# def delete_task(request,id):
#     task=models.TaskCategory.objects.get(pk=id)
                        
#     task.delete()                             
#     return redirect('home')   

