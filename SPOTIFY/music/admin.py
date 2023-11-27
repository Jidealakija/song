from django.contrib import admin
from .models import Artist, Song

# Register your models here.

class ContactSong(admin.ModelAdmin):
    list_display = ['title', 'artist', 'duration']
    list_filter = ['artist']
    


admin.site.register(Artist)
admin.site.register(Song, ContactSong)


