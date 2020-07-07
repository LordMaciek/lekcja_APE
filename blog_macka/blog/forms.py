from django import forms
from .models import BlogEntry, Picture


class CreateNewPost(forms.ModelForm):
    pictures = forms.ModelMultipleChoiceField(queryset=Picture.objects.all(), label="Wybierz zdjęcia")
    title = forms.CharField(max_length=150, label="Tytuł wpisu")
    body = forms.CharField(label="Treść wpisu")

    class Meta:
        model = BlogEntry
        fields = (
            'title',
            'body',
            'pictures',
        )
#     'pictures',

class PhotoAddForm(forms.ModelForm):
    # entry = forms.ModelChoiceField(
    #     queryset=BlogEntry.objects.all(),
    #     widget=forms.HiddenInput(),
    # )

    class Meta:
        model = Picture
        fields = ('title', 'author', 'pic')