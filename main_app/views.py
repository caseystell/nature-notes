import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Campsite, Amenity, Photo
from .forms import TrailForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# @login_required
def campsites_index(request):
    campsites = Campsite.objects.filter(user=request.user)
    return render(request, 'campsites/index.html', 
        {'campsites': campsites
    })

# @login_required
def campsites_detail(request, campsite_id):
    campsite = Campsite.objects.get(id=campsite_id)
    id_list = campsite.amenities.all().values_list('id')
    amenities_campsite_doesnt_have = Amenity.objects.exclude(id__in=id_list)
    trail_form = TrailForm()
    return render(request, 'campsites/detail.html', {
        'campsite': campsite, 'trail_form': trail_form, 'amenities': amenities_campsite_doesnt_have
    })


class CampsiteCreate(CreateView):
    model = Campsite
    fields = ['name', 'location', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CampsiteUpdate(UpdateView):
    model = Campsite
    fields = ['location', 'description']


class CampsiteDelete(DeleteView):
    model = Campsite
    success_url = '/campsites'


# @login_required
def add_trail(request, campsite_id):
    form = TrailForm(request.POST)
    if form.is_valid():
        new_trail = form.save(commit=False)
        new_trail.campsite_id = campsite_id
        new_trail.save()
    return redirect('detail', campsite_id=campsite_id)


# @login_required
def add_photo(request, campsite_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, campsite_id=campsite_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  return redirect('detail', campsite_id=campsite_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)