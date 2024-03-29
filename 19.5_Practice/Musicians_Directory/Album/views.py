from django.shortcuts import render,redirect
from .import forms,models
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

# def Add_Album(request):
#     if request.method=="POST":          #User Post Request dise
#         add_Album=forms.AlbumForm(request.POST) #form er data gulu nilam
#         if add_Album.is_valid():
#             add_Album.save()
#             return redirect('home')
#     else:
#          add_Album=forms.AlbumForm 
#     return render(request,'Add_Album.html',{'form': add_Album})

@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model=models.Album_Model
    form_class=forms.AlbumForm
    template_name='Add_Album.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



# def edit_Album(request,id):
#     album=models.Album_Model.objects.get(pk=id)
#     album_form=forms.AlbumForm(instance=album)
#     if request.method=='POST':                               # User post request koreche
#         album_form=forms.AlbumForm(request.POST,instance=album)               # user theke data gulu nilam
#         if album_form.is_valid():                            # data gula valid kina check korlam
#             album_form.save()                                 # data jodi valid hoy tahole database e save korlam
#             return redirect('home')                      # sob thik thak thakle same url e pathai dilam
#                         # jodi post request na kora hoy tahole user blank page pabe 
#     return render(request,'Add_Album.html',{'form': album_form})

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.Album_Model
    form_class = forms.AlbumForm
    template_name = 'Add_Album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')





def Delete_Album(request,id):
    album=models.Album_Model.objects.get(pk=id)
                            
    album.delete()                               
    return redirect('home')


# @method_decorator(login_required, name='dispatch')
# class DeletePostView(DeleteView):
#     model = models.Album_Model
#     template_name = 'home.html'
#     success_url = reverse_lazy('home')
#     pk_url_kwarg = 'id'
