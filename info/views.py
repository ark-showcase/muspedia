from django.shortcuts import render
from django.http import HttpResponse
from info.models import Musician, Album
from info import forms

# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    dict = {'title': "Muspedia", 'musician_list': musician_list}
    return render(request, 'info/index.html' ,context = dict)



def album_list(request):
    album_list = Album.objects.order_by('release_date','name')
    dict = {'title': "Albums", 'album_list': album_list}
    return render(request, 'info/album_list.html', context = dict)



def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    dict = {'title': "Add Musician", 'musician_form':form}
    return render(request, 'info/musician_form.html', context = dict)



def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    dict = {'title': "Add Album", 'album_form': form}
    return render(request, 'info/album_form.html', context = dict)



def musician_detail(request, musician_id):
    musician_info = Musician.objects.get(id = musician_id)
    musician_albums = Album.objects.filter(artist_id = musician_id)
    dict = {'title': musician_info, 'musician_info': musician_info, 'musician_albums': musician_albums}
    return render(request, 'info/musician_detail.html', context=dict)



def album_detail(request, album_id):
    album_info = Album.objects.get(id = album_id)
    print("artist_id: "+str(album_info.artist_id))
    album_musician = Musician.objects.get(id = album_info.artist_id)
    dict = {'title': album_info.name, 'album_info': album_info, 'album_musician': album_musician}
    return render(request, 'info/album_detail.html', context=dict)



def update_musician(request,id):
    musician = Musician.objects.get(pk=id)
    form = forms.MusicianForm(instance=musician)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=musician)

        if form.is_valid():
            form.save(commit=True)
            return musician_detail(request, id)

    dict = {'title': "Update " + str(musician), 'form': form}
    return render(request, 'info/update_musician.html', context=dict)



def update_album(request,id):
    album = Album.objects.get(pk=id)
    form = forms.AlbumForm(instance=album)

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album)

        if form.is_valid():
            form.save(commit=True)
            return album_detail(request, id)

    dict = {'title': "Update " + str(album.name), 'form': form}
    return render(request, 'info/update_album.html', context=dict)



def delete_album(request,id):
    album = Album.objects.get(pk=id).delete()
    return album_list(request)



def delete_musician(request,id):
    musician = Musician.objects.get(pk=id).delete()
    return index(request)