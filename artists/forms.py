from django import forms
from .widgets import CustomClearableFileInput

from .models import Artist


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = '__all__'
    
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
