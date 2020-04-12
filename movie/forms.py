from django import forms
from .models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'image', 'director','cast','description','release_date']