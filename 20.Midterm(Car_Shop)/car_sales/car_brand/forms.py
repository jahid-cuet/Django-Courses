from django import forms
from .models import Brand

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields='__all__'
        