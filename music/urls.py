from django.urls import path

from . import views

urlpatterns = [
  path('', views.musician_list, name= 'musician'),
  path("musician/<int:musician_id>/", views.album_list, name= "album_list"),
  path("album/<int:album_id>/", views.album_details, name = "album_details")
]