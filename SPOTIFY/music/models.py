from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='artist_image', blank=True, null=True )
    details = models.TextField()

    class Meta:
        verbose_name_plural = 'Artists'

    def __str__(self):
        return self.name
    

class Song(models.Model):
    title = models.CharField(max_length=200)
    duration = models.TimeField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="track_images")
    other_artists = models.CharField(max_length=300)
    release_date = models.DateField()

    def __str__(self):
        return self.title