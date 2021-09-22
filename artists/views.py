from django.shortcuts import render
from .models import Artist

def all_artists(request):

    artists = Artist.objects.all()

    context = {
        'artists': artists
    }

    return render(request, 'artists/artists.html', context)
