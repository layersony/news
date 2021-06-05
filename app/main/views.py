from flask import render_template
from . import main
from ..request import get_sources

@main.route('/')
def index():
  general_source = get_sources('general')
  return render_template('index.html', general = general_source)
