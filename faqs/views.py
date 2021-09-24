from django.shortcuts import render


def faqs(request):
    return render(request, 'faqs/faqs.html')
