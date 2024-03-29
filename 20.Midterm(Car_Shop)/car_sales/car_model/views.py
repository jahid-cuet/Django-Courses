from django.shortcuts import render,redirect
from  .import forms
from  .import models
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from .models import Car,Order
from django.contrib import messages



class DetailPostView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = post
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
    

@login_required
def buy_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        if car.quantity > 0:
            # Handle purchase logic
            car.quantity -= 1
            car.save()
            # Create an order
            Order.objects.create(user=request.user, car=car)
            return redirect('Profile')  # Redirect to the profile page after purchase
        else:
            # Handle out of stock scenario
            messages.error(request, "Sorry, this car is out of stock.")
            return redirect('post_details', car_id=car_id)
    else:
        return render(request, 'post_details.html', {'car': car})
