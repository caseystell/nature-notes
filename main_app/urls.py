from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('campsites/', views.campsites_index, name='index'),
    path('campsites/<int:campsite_id>/', views.campsites_detail, name='detail'),
]