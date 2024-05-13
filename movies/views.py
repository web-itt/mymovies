from django.shortcuts import render
from .models import Movie
# Create your views here.

def list_movies(request):
	movies = Movie.objects.all()
	return render(request,"index.html",{"movies":movies})

def detail_movie(request,id):
	movie = Movie.objects.get(pk=id)
	return render(request,"movie_detail.html",{"movie":movie})
