from django.shortcuts import render,redirect
from  .import forms
from  .import models
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView



# (1)This is Add_Post Section


# Add Post using function view

def Add_Post(request):
    if request.method=='POST':                   # User post request koreche
        post_form=forms.PostForm(request.POST)   # user theke data gulu nilam
        if  post_form.is_valid(): 
            post_form.instance.author=request.user               # data gula valid kina check korlam
            post_form.save()                     # data jodi valid hoy tahole database e save korlam
            return redirect('add_Post')          # sob thik thak thakle same url e pathai dilam
    else:
           post_form=forms.PostForm()           # jodi post request na kora hoy tahole user blank page pabe 
    return render(request,'Add_Post.html',{'form': post_form})



# Add Post using class Based view
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model=models.Post
    form_class=forms.PostForm
    template_name='Add_Post.html'
    success_url = reverse_lazy('Add_Post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)






# (2)This is Edit_Post Section
    

   
 # Edit  using function view
@login_required
def edit_Post(request,id):
    post=models.Post.objects.get(pk=id)
    post_form=forms.PostForm(instance=post)
    if request.method=='POST':                               # User post request koreche
        post_form=forms.PostForm(request.POST,instance=post)               # user theke data gulu nilam
        if  post_form.is_valid(): 
            post_form.instance.author=request.user                             # data gula valid kina check korlam
            post_form.save()                                 # data jodi valid hoy tahole database e save korlam
            return redirect('home')                      # sob thik thak thakle same url e pathai dilam
                        # jodi post request na kora hoy tahole user blank page pabe 
    return render(request,'Add_Post.html',{'form': post_form})



 # Add Post using class based view
@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'Add_Post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('Profile')


# (3)This is Delete_Post Section
    
# Add Post using function based view
@login_required
def delete_Post(request,id):
    post=models.Post.objects.get(pk=id)
                         
    post.delete()                              
    return redirect('home')                      
                        

# Add Post using class based view
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('Profile')
    pk_url_kwarg = 'id'


class DetailPostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context