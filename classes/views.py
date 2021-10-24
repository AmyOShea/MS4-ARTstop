from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.functions import Lower

from .models import Class, Level
from .forms import ClassForm


def all_classes(request):
    """
    View to return all classes
    including filtering & sorting
    """

    classes = Class.objects.all()
    levels = None
    sort = None
    direction = None

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            classes = classes.annotate(lower_name=Lower('name'))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        classes = classes.order_by(sortkey)

    if 'level' in request.GET:
        levels = request.GET['level'].split(',')
        classes = classes.filter(level__name__in=levels)
        levels = Level.objects.filter(name__in=levels)

    current_sorting = f'{sort}_{direction}'

    context = {
        'classes': classes,
        'current_levels': levels,
        'current_sorting': current_sorting,
    }

    return render(request, 'classes/classes.html', context)


def class_detail(request, class_id):
    """ A view to show class details """

    # can't use 'class' as variable name as is reserved word
    a_class = get_object_or_404(Class, pk=class_id)

    context = {
        # changing 'a_class' to 'class' as it can be use in HTML template
        'class': a_class,
    }

    return render(request, 'classes/class_detail.html', context)


@login_required
def add_class(request):
    """ Add classes """
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


@login_required
def edit_class(request, class_id):
    """ Edit classes """

    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to do that.')
        return redirect(reverse('home'))

    a_class = get_object_or_404(Class, pk=class_id)
    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES, instance=a_class)
        if form.is_valid():
            a_class = form.save()
            messages.success(request, 'Class Updated')
            return redirect(reverse('class_detail', args=[a_class.id]))
        else:
            messages.error(request, 'Failed to update class. \
                Please ensure the form is valid.')
    else:
        form = ClassForm(instance=a_class)

    template = 'classes/edit_class.html'
    context = {
        'form': form,
        'class': a_class,
    }

    return render(request, template, context)


@login_required
def delete_class(request, class_id):
    """ Delete classes """

    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to do that.')
        return redirect(reverse('home'))

    a_class = get_object_or_404(Class, pk=class_id)
    a_class.delete()
    messages.success(request, 'Class Deleted')

    return redirect(reverse('classes'))
