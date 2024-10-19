import string
import random

class URLShortener:
    def generate_short_url(self): # generates random string for shortened url.
        characters = string.ascii_letters + string.digits
        short_url = ''
        for i in range(6):
            short_url += random.choice(characters)
        return short_url
