from django import forms
from .models import Discs

class DiscsForm(forms.ModelForm):
    class Meta:
        model = Discs
        fields = '__all__'
