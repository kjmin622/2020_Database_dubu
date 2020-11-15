from django import forms
from .models import *

class adminLoginForm(forms.ModelForm):
    class Meta:
        model = staff
        fields = ['staff_id']