from django import forms
from posts.models import Post

# Create the form class
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"