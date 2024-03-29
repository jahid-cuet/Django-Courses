from django.shortcuts import render

def index(request):


    data=[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere" ,
    "body": "quia et suscipit"
  },

  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore"
  },
  {
    "userId": 1,
    "id": 3,
    "title": "ea molestias quasi",
    "body": "et iusto sed quo "
  },
  {
    "userId": 1,
    "id": 4,
    "title": "eum et est occaecati",
    "body": "ullam et saepe reiciendis "
  },
  {
    "userId": 1,
    "id": 5,
    "title": "nesciunt quas odio",
    "body": "repudiandae veniam quaera"
  },
  {
    "userId": 1,
    "id": 6,
    "title": "dolorem eum magni eos aperiam quia",
    "body": "ut aspernatur"
  },
    ]
    return render(request,'index.html',{'data': data})


def about(request,id):
    return render(request,'index.html',{'id': id})

