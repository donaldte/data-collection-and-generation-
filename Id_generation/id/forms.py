from .models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields=[
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['identification', 'pwd', 'rpwd']



# make with heart by Donald