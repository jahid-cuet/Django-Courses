from django.db import models

# Create your models here.
class TaskCategory(models.Model):
    Category_Name=models.CharField(max_length=30)
    def __str__(self) :
       return f"{self.Category_Name}"
    


    # username--hasan  ,password--575