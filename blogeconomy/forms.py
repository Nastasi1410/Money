from django import forms
from .models import User

class User (forms.Form):

    Name=forms.CharField()
    Category = forms.CharField(max_length=400)
    Purpose = forms.CharField(max_length=400)
    Password = forms.CharField(max_length=400)
    Salary = forms.IntegerField()