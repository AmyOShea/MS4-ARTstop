from django import forms
from .widgets import CustomClearableFileInput

from .models import Class


class ClassForm(forms.ModelForm):

    class Meta:
        model = Class
        fields = '__all__'

    cover_image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)
