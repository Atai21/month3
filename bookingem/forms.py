from django import forms
from . import models
from .models import Comment

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Books
        fields = [
            'title',
            'description'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text'
        ]


