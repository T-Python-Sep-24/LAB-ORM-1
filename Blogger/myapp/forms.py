from django import forms
from myapp.models import post

# Create the form class.
class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = "__all__"
        widgets = {
            'title' : forms.TextInput({"class" : "form-control"})
        }