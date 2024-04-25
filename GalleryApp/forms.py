from django import forms
from .models import Django


        
class DjangoForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Django', 'Django'),
        
    ]
     # Add category field
    
    class Meta:
        model = Django
        fields = ['title', 'image', 'author','about']  # Add category field to the form