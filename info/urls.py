from django.conf.urls import url
from django.urls import path
from info import views

app_name = "info"

urlpatterns = [
    path('',views.index, name = "index"),
    path('albums/', views.album_list, name = "album_list"),
    path('add_album/', views.album_form, name = "album_form"),
    path('add_musician/', views.musician_form, name = "musician_form"),
    path('musician_detail/<int:musician_id>/', views.musician_detail, name='musician_detail'),
    path('album_detail/<int:album_id>/', views.album_detail, name='album_detail'),
    path('update_musician/<int:id>/', views.update_musician, name="update_musician"),
    path('update_album/<int:id>/', views.update_album, name="update_album"),
    path('delete_album/<int:id>/', views.delete_album, name="delete_album"),
    path('delete_musician/<int:id>/', views.delete_musician, name="delete_musician")
]