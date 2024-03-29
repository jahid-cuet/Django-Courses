from django.shortcuts import render
from Album.models import Album_Model
def home(request):
    data=Album_Model.objects.all()

    return render(request,'home.html',{'data':data})

# Create your views here.