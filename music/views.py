
from django.shortcuts import render,get_object_or_404
from .models import Album,Song


def index(request):
   albums=Album.objects.all()

   context={
   'albums': albums,
   }

   return(render(request,"music/index.html",context))

def details(request,album_id):
         album=get_object_or_404(Album,pk=album_id)
         return render(request,"music/details.html",{'album': album})

def favorite(request,album_id):
         album=get_object_or_404(Album,pk=album_id)
         try:
             selected_song=album.song_set.get(pk=request.POST["song"])
         except(KeyError,Song.DoesNotExist):
             return   render(request,"music/details.html",{'album': album, 'error_message': "you did not selected a valid song",})
         else:
                  if (selected_song.favorite==True):
                        selected_song.favorite=False
                        selected_song.save()
                  else:
                       selected_song.favorite= True
                       selected_song.save()

         return render(request,"music/details.html",{'album': album})
