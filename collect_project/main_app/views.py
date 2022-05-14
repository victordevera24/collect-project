from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

import logging
logging.basicConfig(level=logging.DEBUG)

class Fish:
    def __init__(self, name, size, description):
        self.name = name
        self.size = size
        self.description = description

fish = [
    Fish('Exclamation Point Rasbora', '1 inch', 'Exclamation Point positioned horizontally down side of fish'),
    Fish('Celestial Pearl Danio', '1.5 inches', 'Dark blue body with small random white spots covering body'),
    Fish('Otocinclus', '2 inches', 'Eats organisms off surfaces using sucker mouth.')
]

# Define the home view
def home(request):
    """
    home view 
    http://localhost:8000/
    """
    return render(request, 'index.html')

def about(request):
    """
    about view
    http://localhost:8000/about
    """
    return render(request, 'about.html')

def fish_index(request):
    """
    fish index pages
    http://localhost:8000/fish/
    """
    logging.info('calling fish_index')
    return render(request, 'fish/index.html', {'fish' : fish})