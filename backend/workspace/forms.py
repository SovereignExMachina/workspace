from django import forms
from .models import WorkSpace, Column, Task


class WorkSpaceForm(forms.ModelForm):
    class Meta:
        model = WorkSpace
        fields = ('title', 'discription')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'discription': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 5
            }),
        }


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            })
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'discription', 'deadline')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'discription': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 5
            }),
        }