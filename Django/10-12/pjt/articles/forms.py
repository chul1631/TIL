from django import forms
from .models import User
from .models import Article
from django.contrib.auth.forms import UserCreationForm

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        models = User
        fields = UserCreationForm.Meta.fields