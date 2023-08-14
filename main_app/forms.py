from django.forms import ModelForm
from .models import Trail, Amenity 

class TrailForm(ModelForm):
  class Meta:
    model = Trail
    fields = ['name', 'length', 'description']

class AmenityForm(ModelForm):
  class Meta:
    model = Amenity
    fields= ['name']