from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)