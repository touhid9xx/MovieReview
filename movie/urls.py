
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('movie/<int:id>/', views.details, name = 'movie'),
    path('addmovie/', views.createMovie, name = 'add-movie'),   
    path('editmovie/<int:id>/', views.editMovie, name = 'edit-movie'), 
    path('deletemovie/<int:id>/', views.deleteMovie, name = 'delete-movie'),
]