from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


from django.test import LiveServerTestCase
from .models import Place

class TitleTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls): #Arrange
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10) #wait 10 seconds before testing
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()


    def test_title_on_home_page(self):
        self.selenium.get(self.live_server_url)
        self.assertIn('Travel Wishlist',self.selenium.title)

        

class AddPlacesTest(LiveServerTestCase):
    fixtures = ['test_places']
    
    @classmethod
    def setUpClass(cls): #Arrange
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10) #wait 10 seconds before testing
        
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_add_new_places(self):
        self.selenium.get(self.live_server_url)
        input_name = self.selenium.find_element_by_id('id_name') #unique id
        input_name.send_keys('Denver')

        add_button = self.selenium.find_element_by_id('add-new-place')
        add_button.click()

        denver = self.selenium.find_element_by_id('place-name-5')
        self.assertEqual('Denver',denver.text)

        #check other places are also in the page
        self.assertIn('Denver', self.selenium.page_source)
        self.assertIn('New York', self.selenium.page_source)
        self.assertIn('Tokyo', self.selenium.page_source)