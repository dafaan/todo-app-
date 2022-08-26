from django import forms
from django.db import models

from .models import *
  
# create a ModelForm
class tdForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = events
        fields = "__all__"