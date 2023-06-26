from django import forms
from .models import WorkSpace, Column


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
