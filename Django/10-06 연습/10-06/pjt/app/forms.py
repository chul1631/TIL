from django import forms
from . models import App

class AppForms(forms.ModelForm):
	class Meta: 
		model = App
		fields = ['title','summary','runningtime']