from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('campsites/', views.campsites_index, name='index'),
    path('campsites/<int:campsite_id>/', views.campsites_detail, name='detail'),
    path('campsites/create/', views.CampsiteCreate.as_view(), name='campsites_create'),
    path('campsites/<int:pk>/update/', views.CampsiteUpdate.as_view(), name='campsites_update'),
    path('campsites/<int:pk>/delete/', views.CampsiteDelete.as_view(), name='campsites_delete'),
    path('campsites/<int:campsite_id>/add_trail/', views.add_trail, name='add_trail'),
    path('campsites/<int:campsite_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),

]