from django.shortcuts import render,redirect
from  .import forms
from  .import models
def Add_Post(request):
    if request.method=='POST':                   # User post request koreche
        post_form=forms.PostForm(request.POST)   # user theke data gulu nilam
        if  post_form.is_valid():                # data gula valid kina check korlam
            post_form.save()                     # data jodi valid hoy tahole database e save korlam
            return redirect('add_Post')          # sob thik thak thakle same url e pathai dilam
    else:
           post_form=forms.PostForm()           # jodi post request na kora hoy tahole user blank page pabe 
    return render(request,'Add_Post.html',{'form': post_form})
# Create your views here.


def edit_Post(request,id):
    post=models.Post.objects.get(pk=id)
    post_form=forms.PostForm(instance=post)
    if request.method=='POST':                               # User post request koreche
        post_form=forms.PostForm(request.POST,instance=post)               # user theke data gulu nilam
        if  post_form.is_valid():                            # data gula valid kina check korlam
            post_form.save()                                 # data jodi valid hoy tahole database e save korlam
            return redirect('home')                      # sob thik thak thakle same url e pathai dilam
                        # jodi post request na kora hoy tahole user blank page pabe 
    return render(request,'Add_Post.html',{'form': post_form})


def delete_Post(request,id):
    post=models.Post.objects.get(pk=id)
    # post_form=forms.PostForm(instance=post)
    # if request.method=='POST':                               # User post request koreche
    #     post_form=forms.PostForm(request.POST,instance=post)               # user theke data gulu nilam
    #     if  post_form.is_valid():                            # data gula valid kina check korlam
    post.delete()                               # data jodi valid hoy tahole database e save korlam
    return redirect('home')                      # sob thik thak thakle same url e pathai dilam
                        # jodi post request na kora hoy tahole user blank page pabe 
    # return render(request,'Add_Post.html',{'form': post_form})