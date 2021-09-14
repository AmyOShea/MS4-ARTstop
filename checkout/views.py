from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout_view(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JGj02HGScEvSGff2FjDagV7zRVSUvxl35E57yGOEV3Os3TdPPnHqwOy01TxZwkPDnLlqcV5IQRTVflZEcb8V4Gc00SXb7PiCS',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)


def signin_guest(request):
    return render(request, 'checkout/signin-or-guest.html')
