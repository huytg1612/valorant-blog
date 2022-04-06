from django import forms
from django.forms import ModelForm

from blog.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']