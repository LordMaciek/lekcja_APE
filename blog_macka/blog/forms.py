from django import forms
from .models import BlogEntry, Picture


class CreateNewPost(forms.ModelForm):

    class Meta:
        model = BlogEntry
        fields = ('title', 'body',)


class PhotoAddForm(forms.ModelForm):
    # entry = forms.ModelChoiceField(
    #     queryset=BlogEntry.objects.all(),
    #     widget=forms.HiddenInput(),
    # )

    class Meta:
        model = Picture
        fields = ('title', 'author', 'pic')
