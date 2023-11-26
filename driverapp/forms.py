from django import forms
from django.contrib.auth.models import User

from .models import *


class DriverInformationForm(forms.ModelForm):
    class Meta:
        model = BusInformation
        exclude = ('is_public',)


class UserDriverForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
