from django.db import models
from category .models import TaskCategory

# Create your models here.
class TaskModel(models.Model):
    taskTitle=models.CharField(max_length=50)
    taskDescription = models.TextField()
    is_completed =models.BooleanField(default=False)
    category=models.ManyToManyField(TaskCategory)
    Task_Assigned_Date=models.DateField()
    def __str__(self) :
        return f"{self.taskTitle}"
