from django.shortcuts import render
import datetime
def home(request):
    d={'author': 'jahid', 'age':20, 'Roll' :1911018,'list':['Python','is','Best'], 'birthday': datetime.datetime.now() ,'courses':[
        { 'name':'cse',
        'id':1} ,
        { 'name':'mse',
        'id':2} ,
        { 'name':'bme',
        'id':3} ,
    ]
       

    }


    return render(request,'first_app/home.html',d)

# Create your views here.
