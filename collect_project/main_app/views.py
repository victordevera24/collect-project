from django.shortcuts import render
from .models import Fish

# Add the following import
from django.http import HttpResponse

import logging
logging.basicConfig(level=logging.DEBUG)


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
    fish = Fish.objects.all()
    return render(request, 'fish/index.html', {'fish' : fish})