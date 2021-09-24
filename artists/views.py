from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import Artist
from products.models import Product
from .forms import ArtistForm


def all_artists(request):

    artists = Artist.objects.all()
    context = {
        'artists': artists
    }

    return render(request, 'artists/artists.html', context)


def artist_detail(request, artist_id):

    artist = get_object_or_404(Artist, pk=artist_id)
    products = Product.objects.all()

    context = {
        'artist': artist,
        'products': products,
    }

    return render(request, 'artists/artist_detail.html', context)


def add_artist(request):

    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save()
            messages.success(request, 'Artist added')
            return redirect(reverse('artist_detail', args=[artist.id]))
        else:
            messages.error(request, 'Failed to add Artist. \
                Please endure form is valid')
    else:
        form = ArtistForm()

    template = 'artists/add_artist.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_artist(request, artist_id):
 
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to do that.')
        return redirect(reverse('home'))

    artist = get_object_or_404(Artist, pk=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            artist = form.save()
            messages.success(request, 'Artist Updated')
            return redirect(reverse('artist_detail', args=[artist.id]))
        else:
            messages.error(request, 'Failed to update artist. \
                Please ensure the form is valid.')
    else:
        form = ArtistForm(instance=artist)

    template = 'artists/edit_artist.html'
    context = {
        'form': form,
        'artist': artist,
    }

    return render(request, template, context)


def delete_artist(request, artist_id):
    
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to do that.')
        return redirect(reverse('home'))

    artist = get_object_or_404(Artist, pk=artist_id)
    artist.delete()
    messages.success(request, 'Artist Deleted')

    return redirect(reverse('artists'))
