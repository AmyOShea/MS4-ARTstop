from django import forms
from .widgets import CustomClearableFileInput

from .models import Class


class ClassForm(forms.ModelForm):

    class Meta:
        model = Class
        fields = '__all__'

    # Add help_text because required input formate may not be intuitive
    duration = forms.TimeField(help_text='Input format as hh:mm:ss')

    cover_image = forms.ImageField(label='Image', required=True,
                                   widget=CustomClearableFileInput)
