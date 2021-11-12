from django.test import TestCase
from django.urls import reverse #django urls callmethod

from .models import Place

# Create your tests here.
class TestHomePage(TestCase):
    def test_home_page_shows_empty_list_message_for_empty_database(self):
        home_page_url = reverse('place_list')#look by name instead of url
        response = self.client.get(home_page_url)
        self.assertTemplateUsed(response, 'place_wishlist/wishlist.html')
        self.assertTrue(response, 'You have no places in your wishlist')
        
class TestWishList(TestCase):
    """loads test_places fixtures for testing. """
    fixtures = ['test_places']

    def test_viewing_wishlist_contains_not_visited_places(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'place_wishlist/wishlist.html')
        self.assertContains(response, 'Tokyo')
        self.assertContains(response, 'New York')
        self.assertNotContains(response, 'San Francisco')        
        self.assertNotContains(response, 'Moab')



class TestVisitedPage(TestCase):
    def test_visited_page_shows_empty_list_message_for_empty_database(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'place_wishlist/visited.html')
        self.assertContains(response,'You have not visited any places yet.')


class TestVisitedList(TestCase):
    fixtures = ['test_places']
    
    def test_viewing_places_visited_shows_visited_places(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'place_wishlist/visited.html')

        self.assertNotContains(response, 'Tokyo')
        self.assertNotContains(response, 'New York')
        self.assertContains(response, 'San Francisco')        
        self.assertContains(response, 'Moab')


class TestAddNewPlace(TestCase):

    def test_add_new_unvisited_place(self):
        add_place_url = reverse('place_list') #send url data to place_list in views
        new_place_data = {'name': 'Tokyo', 'visited': False }

        response = self.client.post(add_place_url, new_place_data, follow=True) #create post req data and follow the redirect
        
        # Check correct template was used
        self.assertTemplateUsed(response, 'place_wishlist/wishlist.html')

        #check used response
        response_places = response.context['places']
        self.assertEqual(1, len(response_places))
        tokyo_from_res = response_places[0]

        #check same data as the db
        tokyo_in_database = Place.objects.get(name='Tokyo', visited=False)
        self.assertEqual(tokyo_in_database, tokyo_from_res)

        self.assertEqual(tokyo_in_database,tokyo_from_res)

class TestVisitPlace(TestCase):
    fixtures = ['test_places']

    def test_visit_place(self):
        visit_place_url = reverse('place_was_visited', args=(2,))
        response = self.client.post(visit_place_url, follow=True)

        self.assertNotContains(response, 'New York')
        self.assertContains(response, 'Tokyo')

        new_york = Place.objects.get(pk=2)
        self.assertTrue(new_york.visited)

    def test_non_existent_place(self):
        visit_nonexistent_place_url = reverse('place_was_visited', args=(1234567,))
        response = self.client.post(visit_nonexistent_place_url,follow=True)
        self.assertEqual(404, response.status_code)
