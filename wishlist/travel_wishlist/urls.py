""" Handles all of the specific url routes,queries from db or templates that need to be rendered. """ 

from django.urls import path
from. import views 

""" links specific URL(urlpath) to the defined views(urlHandler)."""
#Django runs through each URL path in order, and stops at the first one that matches the requested URL
urlpatterns = [
    path('',views.place_list, name="home"),#can reference specific url by its name
    path('visited', views.places_visited, name="visited"),
    path('place/<int:place_pk>/was_visited/', views.place_was_visited, name='place_was_visited')
]