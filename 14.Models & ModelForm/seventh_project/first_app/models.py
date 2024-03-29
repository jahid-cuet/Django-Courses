from django.db import models


class Student_Model(models.Model):
    roll=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    address=models.TextField(max_length=30)
    Father_name=models.TextField()

    def __str__(self):
        return f'Name: {self.name}'

