from django import forms
from django.contrib.auth.models import User

from .models import PropertyInformation


class PropertyInformationForm(forms.ModelForm):
    class Meta:
        model = PropertyInformation
        exclude = ('is_public', 'is_reserve')


class UserPropertyForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
