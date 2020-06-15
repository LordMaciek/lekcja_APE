from django import forms
from .models import BlogEntry


class CreateNewPost(forms.ModelForm):

    class Meta:
        model = BlogEntry
        fields = ('title', 'body',)
