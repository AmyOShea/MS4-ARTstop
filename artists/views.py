from django.shortcuts import render, get_object_or_404
from .models import Artist
from products.models import Product


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
