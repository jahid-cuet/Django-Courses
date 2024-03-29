from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Category)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/media/uploads/', blank = True, null = True)
    def __str__(self) :
        return f"{self.title}"
    




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # jkhn e ei class er object toiri hobe sei time ta rekhe dibe
    
    def __str__(self):
        return f"Comments by {self.name}"
        