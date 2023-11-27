from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST'])
def all_songs(request):
    if request.method == 'GET':
        all_songs = Song.objects.all()
        serialized_songs = SongSerializer(all_songs, many=True)
        return Response(serialized_songs.data)
    else:
        song_data = SongSerializer(data=request.data)
        if song_data.is_valid():
            song_data.save()
            return Response('New Track has been successfully')
        return Response(song_data.errors)
    

@api_view(['GET', 'PUT', 'DELETE'])
def songs(request, id):
    if request.method == 'GET':
        single_song = Song.objects.get(id=id)
        serialized_song = SongSerializer(single_song)
        return Response(serialized_song.data)
    elif request.method =='PUT':
        single_song = Song.objects.get(id = id)
        serialized_song = SongSerializer(single_song, data=request.data, partial=True)
        if serialized_song.is_valid():
            serialized_song.save()
            return Response('You have successfully updated this track')
        return Response('Something went wrong')
    else:
        single_song = Song.objects.get(id=id)
        single_song.delete()
        return Response('You have successfully the track')
