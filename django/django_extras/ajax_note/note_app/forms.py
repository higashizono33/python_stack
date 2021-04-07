from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    post = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Post
        fields = ['post']