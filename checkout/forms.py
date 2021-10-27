from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode',
                  'country'
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postal Code',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

        # adding regex to each field to avoid whitespace being
        # submitted to Stripe
        self.fields['full_name'].widget.attrs.update(
            {'pattern': '.*\\S+.*'})
        self.fields['phone_number'].widget.attrs.update(
            {'pattern': '.*\\S+.*'})
        self.fields['street_address1'].widget.attrs.update(
            {'pattern': '.*\\S+.*'})
        self.fields['street_address2'].widget.attrs.update(
            {'pattern': '.*\\S+.*'})
        self.fields['town_or_city'].widget.attrs.update(
            {'pattern': '.*\\S+.*'})
        self.fields['county'].widget.attrs.update(
            {'pattern': '.*\\S+.*'})
        self.fields['postcode'].widget.attrs.update(
            {'pattern': '.*\\S+.*'})
