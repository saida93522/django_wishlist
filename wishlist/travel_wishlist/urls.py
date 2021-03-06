""" Handles all of the specific url routes,queries from db or templates that need to be rendered. """ 

from django.urls import path
from. import views , admin_views

""" links specific URL(urlpath) to the defined views(urlHandler)."""
#Django runs through each URL path in order, and stops at the first one that matches the requested URL
urlpatterns = [
    path('',views.place_list, name="place_list"),#can reference specific url by its name
    path('about', views.about, name="about"),
    path('visited', views.places_visited, name="places_visited"),
    path('place/<int:place_pk>/was_visited/', views.place_was_visited, name='place_was_visited'), #pk 
    path('place/<int:place_pk>', views.place_details, name='place_details'), #pk url pattern for POST request catches specfic url page, eg, place/3 or place/2
    path('place/<int:place_pk>/delete', views.delete_place, name='delete_place'),
    path('catfact', admin_views.get_cat_facts, name='admin_get_cat_fact') 
]
