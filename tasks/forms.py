from django import forms
from .models import Task


class TaskForm(forms.Form):
    class Meta:
        model = Task
        fields = ['title', 'detail', 'end_date']
