from django.db import models

class MusicianModel(models.Model):
   First_Name=models.CharField(max_length=20)
   Last_Name=models.CharField(max_length=20)
   Email=models.EmailField()
   Phone_number=models.CharField(max_length=12)
   Instrument_Type=models.CharField(max_length=12)

   def __str__(self) :
        return f"{self.First_Name}"



# Create your models here.
