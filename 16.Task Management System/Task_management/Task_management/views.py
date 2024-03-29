from django.shortcuts import render
from task.models import TaskModel
from category.models import TaskCategory
def home(request):
    data=TaskModel.objects.all()

    return render(request,'home.html',{'data':data})
