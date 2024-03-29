from django.http import HttpResponse


def contact(request):
    return HttpResponse ('THis is my project contact')
def home(request):
    return HttpResponse ('This is my home page')