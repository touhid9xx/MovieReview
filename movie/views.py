from django.shortcuts import get_object_or_404, redirect, render

from .forms import *
from .models import *

# Create your views here.


def index(request):
    movies = Movie.objects.all()

    context = {
        'movies': movies
    }
    return render(request, 'movie/index.html', context)


def details(request, id):
    movie = Movie.objects.get(id=id)

    context = {
        'movie': movie
    }
    return render(request, 'movie/details.html', context)


def createMovie(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            form = MovieForm()
            if request.method == 'POST':
                form = MovieForm(request.POST, request.FILES)
                
                if form.is_valid():
                    movie = form.save()
                    movie.save()
                    return redirect('movie' ,id = movie.id)
                else :
                    form = MovieForm()
        else: 
            return redirect('index')
    else:
        return redirect('login')    
        
    return render(request, 'movie/addmovie.html', {'form': form, 'controller': "Add Movies"})


def editMovie(request, id):
    movie = Movie.objects.get(id=id)
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                form = MovieForm(request.POST or None, instance=movie) 
                if form.is_valid():
                    data = form.save() 
                    data.save()
                return redirect('movie',id)
            else:
                form = MovieForm(instance=movie) 
        else: 
            return redirect('index')
    else:
                return redirect('login')  
    return render(request, 'movie/addmovie.html', {'form': form, 'controller': "Edit Movies"})



def deleteMovie(request, id):
    movie = Movie.objects.get(id=id)
    if request.user.is_authenticated:
        if request.user.is_superuser:


            movie.delete()
            return redirect('index')

        else: 
            return redirect('index')
    else:
        return redirect('login')  