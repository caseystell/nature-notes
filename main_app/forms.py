from django.forms import ModelForm
from .models import Trail

class TrailForm(ModelForm):
  class Meta:
    model = Trail
    fields = ['name', 'length', 'description']