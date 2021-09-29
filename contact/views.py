from django.shortcuts import render

from .forms import ContactForm


def contact(request):

    form = ContactForm()

    context = {
        'form': form,
    }

    template = 'contact/contact.html'
    return render(request, template, context)
