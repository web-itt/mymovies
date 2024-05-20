from django.shortcuts import render, redirect
from .models import Movie,MovieReview
from .forms import LoginForm,CreateReviewForm
from django.contrib.auth import authenticate, login,logout,get_user_model
from django.shortcuts import get_object_or_404

    
def list_movies(request):
	movies = Movie.objects.all()
	return render(request,"index.html",{"movies":movies})

def detail_movie(request,id):
	form = CreateReviewForm()
	if request.method == 'POST':
		if not request.user.is_authenticated:
			return redirect('login')

		form = CreateReviewForm(data=request.POST)
		if form.is_valid():
			raiting = form.cleaned_data.get('rating')
			description = form.cleaned_data.get('description')
			
			user_id = request.user.id
			User = get_user_model()
			user = get_object_or_404(User, pk=user_id)
			
			movie = get_object_or_404(Movie, pk=id)
			
			user_review = MovieReview.objects.create(user=user,movie=movie,rating=raiting,review=description)
			
			return redirect('movie', id=id)
	else:
		movie = Movie.objects.get(pk=id)
		comments = MovieReview.objects.filter(movie_id=id)
		return render(request,"movie_detail.html",{"movie":movie,"form":form,"comments":comments})

def render_login(request):
	if request.method == 'POST':
		form = LoginForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
		else:
			return render(request, 'login.html', {'form': form})
	else:
		form = LoginForm()
		
		
	return render(request, 'login.html',{"form": form})
	
def render_logout(request):
	logout(request)
	return redirect('home')
	

