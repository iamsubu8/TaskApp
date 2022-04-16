
from django import forms
from .models import *
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        labels = {
            "username":"UserID",
            "password":"Password"
        }
        widget = { #widget will help to add attributes to the html templates form
            "username": forms.TextInput(attrs={'class':'form-control'}),
            "password": forms.PasswordInput(attrs={'class':'form-control'})
        }

class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = TaskStatusTable
        fields = ['TaskID','TStatus']

class TaskForm(forms.ModelForm):
    class Meta:
        model = TasksTable
        fields = '__all__'
