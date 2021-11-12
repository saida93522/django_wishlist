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