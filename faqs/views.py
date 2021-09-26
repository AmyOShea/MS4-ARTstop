from django.shortcuts import render
from django.conf import settings


def faqs(request):

    free_delivery = settings.FREE_DELIVERY_THRESHOLD
    delivery_cost = settings.STANDARD_DELIVERY
    template = 'faqs/faqs.html'

    context = {
        'free_delivery': free_delivery,
        'delivery_cost': delivery_cost
    }

    return render(request, template, context)
