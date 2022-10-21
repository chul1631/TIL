from django import forms
from .models import User

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['user','email','password1','password2']
        


        