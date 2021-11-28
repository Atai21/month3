from .models import BlogPost
from django.forms import ModelForm, TextInput, FileInput

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'description',]

        widgets = {
            "title": TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Заголовок'
            }),
            "description": TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Описание'
            }),
            "image": FileInput(attrs={
                "class": 'form-control',
            })
        }