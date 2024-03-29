from django.db import models
from musician .models import MusicianModel
class Album_Model(models.Model):
    Album_name=models.CharField(max_length=20)
    musician=models.ForeignKey(MusicianModel,on_delete=models.CASCADE)
    Album_release_date=models.DateTimeField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

# Create your models here.
    def __str__(self) :
        return f"{self.Album_name}"