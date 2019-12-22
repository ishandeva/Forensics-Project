from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.Field()
    last_name = forms.Field()

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

class ProfileForm(forms.Form):
    username= forms.Field()
    email = forms.EmailField()
    first_name = forms.Field()
    last_name = forms.Field()

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
