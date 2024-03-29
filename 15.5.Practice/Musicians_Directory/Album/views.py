from django.shortcuts import render,redirect
from .import forms,models

def Add_Album(request):
    if request.method=="POST":          #User Post Request dise
        add_Album=forms.AlbumForm(request.POST) #form er data gulu nilam
        if add_Album.is_valid():
            add_Album.save()
            return redirect('home')
    else:
         add_Album=forms.AlbumForm 
    return render(request,'Add_Album.html',{'form': add_Album})



def edit_Album(request,id):
    album=models.Album_Model.objects.get(pk=id)
    album_form=forms.AlbumForm(instance=album)
    if request.method=='POST':                               # User post request koreche
        album_form=forms.AlbumForm(request.POST,instance=album)               # user theke data gulu nilam
        if album_form.is_valid():                            # data gula valid kina check korlam
            album_form.save()                                 # data jodi valid hoy tahole database e save korlam
            return redirect('home')                      # sob thik thak thakle same url e pathai dilam
                        # jodi post request na kora hoy tahole user blank page pabe 
    return render(request,'Add_Album.html',{'form': album_form})


def Delete_Album(request,id):
    album=models.Album_Model.objects.get(pk=id)
                            
    album.delete()                               
    return redirect('home')

