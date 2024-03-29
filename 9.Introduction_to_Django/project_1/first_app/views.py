from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse ('this is my App Home page')
def about(request):
    return HttpResponse ('this is my App about page')
# Create your views here.
