from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(widget=forms.PasswordInput, label="Hasło")


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='hasło',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='powtórz hasło',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie pokrywają się!')
        return cd['password2']
