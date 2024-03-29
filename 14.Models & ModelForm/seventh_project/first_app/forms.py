from django import forms   
from first_app.models import Student_Model

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student_Model
        fields='__all__'
        labels={
            'name':'Student Name',
            'roll':'Student Roll'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'btn-primary'}),
            'roll':forms.PasswordInput()
        }

