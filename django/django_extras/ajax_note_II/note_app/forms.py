from django import forms
from django.forms import ModelForm
from .models import Note

class NoteForm(ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Note
        fields = ['title', 'content']

# class UpdateForm(ModelForm):
#     title = forms.CharField(initial='')
#     content = forms.CharField(widget=forms.Textarea, label='', initial='')
#     class Meta:
#         model = Note
#         fields = ['title', 'content']