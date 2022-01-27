from .models import UserProfile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'Born_year',)



# make with heart by Donald