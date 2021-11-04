from django.apps import AppConfig
"""let django know about the app """

class TravelWishlistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'travel_wishlist'
