from flask import Blueprint, request, jsonify, redirect
from app.models import URL
from app.utils import URLShortener
from app import db

class URLRoutes:
    def __init__(self):
        self.routes = Blueprint('routes', __name__) 
        self.url_shortener = URLShortener() # initializes url shortener utility

        # defines routes
        self.routes.add_url_rule('/shorten', 'shorten_url', self.shorten_url, methods=['POST'])
        self.routes.add_url_rule('/<short_url>', 'redirect_url', self.redirect_url)

    def shorten_url(self):
        original_url = request.json['url']

        existing_url = URL.query.filter_by(original_url=original_url).first()
        if existing_url: # checks to see if long url already has a short url
            return jsonify({'short_url': existing_url.short_url})
        
        short_url = self.url_shortener.generate_short_url()
        new_url = URL(original_url=original_url, short_url=short_url) # generates short url
        db.session.add(new_url)
        db.session.commit()
        return jsonify({'short_url': short_url})

    def redirect_url(self, short_url):
        url = URL.query.filter_by(short_url=short_url).first_or_404() # queries database for original url
        return redirect(url.original_url)