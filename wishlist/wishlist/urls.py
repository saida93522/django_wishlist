"""wishlist project CORE URL Configuration for the whole project.

"""
import debug_toolbar

from django.contrib import admin
from django.urls import path,include


""" links to the app's urls file, which then mapps to work with the defined urlHandler(views). """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('travel_wishlist.urls')),
    path('__debug__/', include(debug_toolbar.urls))
]
