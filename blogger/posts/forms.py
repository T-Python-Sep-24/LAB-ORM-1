from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'is_published']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your content here...'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title here...'}),
        }
        labels = {
            'is_published': 'Publish Post?',
        }
