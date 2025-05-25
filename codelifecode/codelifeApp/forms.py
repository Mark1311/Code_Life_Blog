from django import forms
from .models import CodeLife

class AppForm(forms.ModelForm):
    class Meta:
        model = CodeLife
        fields = ['text', 'photo']