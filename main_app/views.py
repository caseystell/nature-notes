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
from .models import Campsite, Amenity, Trail, Photo

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
    trails = Trail.objects.filter(user=request.user)
    return render(request, 'campsites/detail.html', {
        'campsite': campsite, 'trails': trails, 'amenities': amenities_campsite_doesnt_have
    })


