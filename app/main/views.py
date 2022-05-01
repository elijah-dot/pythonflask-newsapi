from flask import render_template
from . import main
from ..requests import get_sources, get_articles
from ..models_sources import Source
