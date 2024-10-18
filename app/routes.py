from flask import Blueprint, request, jsonify, redirect
from app.models import URLModel
from app.utils import URLShortener
from app import db