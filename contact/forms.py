from django import forms


class Contact(forms.Form):

    contact_type = (
        ("1", "A Customer"),
        ("2", "An Artist")
    )

    name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_as = forms.CharField(choices=contact_type)
    message = forms.CharField(required=True)
