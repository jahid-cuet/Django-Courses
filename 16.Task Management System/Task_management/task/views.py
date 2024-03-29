# Create your views here.

from django.shortcuts import render,redirect
from  .import forms
from  .import models
def Add_Task(request):
    if request.method=='POST':                   # User post request koreche
        task_form=forms.TaskForm(request.POST)   # user theke data gulu nilam
        if  task_form.is_valid():                # data gula valid kina check korlam
            task_form.save()                     # data jodi valid hoy tahole database e save korlam
            return redirect('Add_Task')          # sob thik thak thakle same url e pathai dilam
    else:
           task_form=forms.TaskForm()           # jodi post request na kora hoy tahole user blank page pabe 
    return render(request,'Add_Task.html',{'form': task_form})
# Create your views here.


def edit_task(request,id):
    task=models.TaskModel.objects.get(pk=id)
    task_form=forms.TaskForm(instance=task)
    if request.method=='POST':                               # User post request koreche
        task_form=forms.TaskForm(request.POST,instance=task)               # user theke data gulu nilam
        if  task_form.is_valid():                            # data gula valid kina check korlam
            task_form.save()                                 # data jodi valid hoy tahole database e save korlam
            return redirect('home')                      # sob thik thak thakle same url e pathai dilam
                        # jodi post request na kora hoy tahole user blank page pabe 
    return render(request,'Add_Task.html',{'form': task_form})


def delete_task(request,id):
    task=models.TaskModel.objects.get(pk=id)
                        
    task.delete()                             
    return redirect('home')   