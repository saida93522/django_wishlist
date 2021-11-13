from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
# Create your models here.
""" models(object) holds data in ORM. defines the logical structure behind the entire app.
using CRUD,creates place table that stores user's name and the places user visited or wants to visit """


class Place(models.Model): #place table
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    date_visited = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        """ create or update existing place object. """
        old_place = Place.objects.filter(pk=self.pk).first()
        if old_place and old_place.photo:
            if old_place.photo != self.photo:
                self.delete_photo(old_place.photo)
        super().save(*args, **kwargs)
        
    def delete_photo(self, photo):
        """remove photo from place object. """
        if default_storage.exists(photo.name):
            default_storage.delete(photo.name)

    def delete(self,  *args, **kwargs):
        """remove photo from place object and from media file."""
        if self.photo:
            self.delete_photo(self.photo)
            
        super().delete(*args, **kwargs)

    objects = models.Manager() # provides interface between db query operations and the django model.
    
    def __str__(self):
        photo_str = self.photo if self.photo else 'No Photo Found'
        return f'{self.name}, visited? {self.visited} on {self.date_visited}. Photo {photo_str}'