from .models import Task, Films
from django.forms import ModelForm, TextInput, Textarea
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
class FilmsForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = ['name', 'image']