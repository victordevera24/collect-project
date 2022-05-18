from django.shortcuts import render, redirect
from .models import Fish
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from .forms import FeedingForm

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

def fish_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    feeding_form = FeedingForm()
    return render(request, 'fish/detail.html', { 'fish' : fish, 'feeding_form': feeding_form})

class FishCreate(CreateView):
    model = Fish
    fields = '__all__'
    def get_success_url(self, **kwargs):
        return reverse('detail', args=(self.object.id,))

class FishUpdate(UpdateView):
    model = Fish
    fields = ['description']
    success_url = '/fish/'

class FishDelete(DeleteView):
    model = Fish
    success_url = '/fish/'

def add_feeding(request, fish_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.fish_id = fish_id
        new_feeding.save()
    return redirect('detail', fish_id=fish_id)