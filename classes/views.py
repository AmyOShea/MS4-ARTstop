from django.shortcuts import render, get_object_or_404
from .models import Class


def all_classes(request):

    classes = Class.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'classes/classes.html', context)


def class_detail(request, class_id):

    # can't use 'class' as variable name as is reserved word
    a_class = get_object_or_404(Class, pk=class_id)

    context = {
        # changing 'a_class' to 'class' as it can be use in HTML template
        'class': a_class,
    }

    return render(request, 'classes/class_detail.html', context)