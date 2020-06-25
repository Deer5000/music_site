from django.http import HttpResponse
from django.shortcuts import render
from .models import Musician

def home(request):
    return HttpResponse("Hello, world. This is my music site!")

def classical_songs(request):
    return HttpResponse("Hello Classical!")


def musician_list(request):
    context = {'musicians': Musician.objects.all()}
    return render(request, 'musician_list.html', context)

def album_list(request, musician_id):
    musician =  Musician.objects.get(id = musician_id),
    albums =  musician.album_set.all()
    context = { 'musican': musician, 'albums': albums}
    return render(request, 'musician_details.html', context)