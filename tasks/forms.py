from django import forms
from .models import Task
from django_jalali.admin.widgets import AdminSplitjDateTime


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'details', 'end_date']
        widgets = {
            'end_date': AdminSplitjDateTime
        }
