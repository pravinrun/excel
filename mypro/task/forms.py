from django import forms
from .models import User,Task

class Userf(forms.ModelForm):
    class Meta:
        model = User
        fields =['name','email','mobile']
class Taskf(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'task_detail', 'task_type']
