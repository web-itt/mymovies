from django.urls import path
from . import views

urlpatterns = [
path("",views.list_movies,name="list_movies"),
path("<int:id>",views.detail_movie,name="detail_movie")
]
