from flask import Blueprint, request, jsonify, redirect
from app.models import URL
from app.utils import URLShortener
from app import db
import re
import socket

class URLRoutes:
    def __init__(self):
        self.routes = Blueprint('routes', __name__) 
        self.url_shortener = URLShortener() # initializes url shortener utility

        # defines routes
        self.routes.add_url_rule('/shorten', 'shorten_url', self.shorten_url, methods=['POST'])
        self.routes.add_url_rule('/<short_url>', 'redirect_url', self.redirect_url)

    def shorten_url(self):
        original_url = request.json['url']

        if not original_url.startswith(('http://', 'https://')): # checks to see if url starts with https:// or http://
            original_url = 'https://' + original_url # defaults to https://
        
        pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
        if not re.match(pattern, original_url):
            return jsonify({'error': 'Invalid URL format'}), 400
        
        # extracts domain from url
        domain = original_url.split("//")[-1].split("/")[0]
        
        # checks if to-be-shortened website exists
        try:
            socket.gethostbyname(domain)
        except socket.gaierror:
            return jsonify({'error': 'Provided domain doesn\'t exist'}), 400

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
