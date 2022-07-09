from django import forms
from .models import Category

class InputExpence(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

