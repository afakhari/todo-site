from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django_jalali.admin.widgets import AdminSplitjDateTime
from .models import Task


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    pass


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'details', 'deadline']
        widgets = {
            'deadline': AdminSplitjDateTime
        }
