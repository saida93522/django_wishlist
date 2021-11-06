from django.db import models

# Create your models here.
""" models(object) holds data in ORM. defines the logical structure behind the entire app.
using CRUD,creates place table that stores user's name and the places user visited or wants to visit """


class Place(models.Model): #place table
    # fields
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    objects = models.Manager() # provides interface between db query operations and the django model.
    
    def __str__(self):
        return f'{self.name}: visited? {self.visited}' 