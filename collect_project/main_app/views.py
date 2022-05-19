import uuid
import boto3
import os
from django.shortcuts import render, redirect
from .models import Fish, Toy, Photo
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
    toys_fish_doesnt_have = Toy.objects.exclude(id__in = fish.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'fish/detail.html', {
        'fish' : fish,
        'feeding_form': feeding_form,
        'toys': toys_fish_doesnt_have
    })

class FishCreate(CreateView):
    model = Fish
    fields = ['name', 'size', 'description']
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
        # has the fish_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.fish_id = fish_id
        new_feeding.save()
    return redirect('detail', fish_id=fish_id)

def assoc_toy(request, fish_id, toy_id):
    Fish.objects.get(id=fish_id).toys.add(toy_id)
    return redirect('detail', fish_id=fish_id)

def add_photo(request, fish_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, fish_id=fish_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', fish_id=fish_id)