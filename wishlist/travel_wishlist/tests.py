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

class TestVisitedPage(TestCase):

    def test_visited_page_shows_empty_list_message_for_empty_database(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
        self.assertContains(response, 'You have not visited any places yet')


class TestWishList(TestCase):

    fixtures = ['test_places']

    def test_viewing_wishlist_contains_not_visited_places(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        
        self.assertContains(response, 'Tokyo')
        self.assertContains(response, 'New York')
        self.assertNotContains(response, 'San Francisco')        
        self.assertNotContains(response, 'Moab')


class TestVisitedList(TestCase):

    fixtures = ['test_places']

    def test_viewing_places_visited_shows_visited_places(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')

        self.assertNotContains(response, 'Tokyo')
        self.assertNotContains(response, 'New York')
        self.assertContains(response, 'San Francisco')        
        self.assertContains(response, 'Moab')


class TestAddNewPlace(TestCase):

    def test_add_new_unvisited_place_to_wishlist(self):

        add_place_url = reverse('place_list')
        new_place_data = {'name': 'Tokyo', 'visited': False }

        response = self.client.post(add_place_url, new_place_data, follow=True)
        # Check correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        #check used response
        response_places = response.context['places']
        self.assertEqual(1, len(response_places))
        tokyo_response = response_places[0]

        #check same data as the db
        tokyo_in_database = Place.objects.get(name='Tokyo', visited=False)