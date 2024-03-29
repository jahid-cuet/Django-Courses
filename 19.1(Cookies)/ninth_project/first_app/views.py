from django.shortcuts import render

def home(request):
    response=render(request,'home.html')
    response.set_cookie('name','karim')
    response.set_cookie('name','Rahim')
    return response
def get_cook(request):
    name=request.COOKIES.get('name')
    return render(request,'get_cookie.html',{'name':name})


def delete_cookie(request):
    response=render(request,'del.html')
    response.delete_cookie('name')
    return response 


def set_session(request):
    data={
        'name':'rahim',
        'age':34,
        'language':'bangla'

    }
    request.session.update(data)
    return render('request','home.html')