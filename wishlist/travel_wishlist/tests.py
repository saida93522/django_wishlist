from django.test import TestCase
from django.urls import reverse #django urls callmethod

from .models import Place

# Create your tests here.
class TestHomePage(TestCase):

    
    def test_load_home_page_shows_empty_list_for_empty_database(self):
        home_page_url = reverse('place_list') #look by name instead of url
        response = self.client.get(home_page_url)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')
        self.assertContains(response, 'You have no places in your wishlist.')