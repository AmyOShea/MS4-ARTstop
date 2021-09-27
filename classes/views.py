from django.shortcuts import render
from .models import Class


def all_classes(request):

    classes = Class.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'classes/classes.html', context)