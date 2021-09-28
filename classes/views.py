from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import Class
from .forms import ClassForm


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


def add_class(request):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES)
        if form.is_valid():
            a_class = form.save()
            messages.success(request, 'Class added')
            return redirect(reverse('class_detail', args=[a_class.id]))
        else:
            messages.error(request, 'Failed to add Class. \
                Please ensure form is valid')
    else:
        form = ClassForm()

    template = 'classes/add_class.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
