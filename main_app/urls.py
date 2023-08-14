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
    path('campsites/<int:campsite_id>/add_amenity/<int:amenity_id>/', views.add_amenity, name='add_amenity'),
    path('campsites/<int:campsite_id>/remove_amenity/<int:amenity_id>/', views.remove_amenity, name='remove_amenity'),
    path('amenities/', views.AmenityList.as_view(), name='amenities_index'),
    path('amenities/<int:pk>', views.AmenityDetail.as_view(), name='amenities_detail'),
    path('amenities/create/', views.AmenityCreate.as_view(), name='amenities_create'),
    path('amenities/<int:pk>/delete/', views.AmenityDelete.as_view(), name='amenities_delete'),
    path('accounts/signup/', views.signup, name='signup'),

]

# path('campsites/<int:campsite_id>/add_photo/', views.add_photo, name='add_photo'),