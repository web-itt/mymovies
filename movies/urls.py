from django.urls import path
from . import views

urlpatterns = [
    path("",views.list_movies,name="home"),
    path("<int:id>",views.detail_movie,name="movie"),
    path("login",views.render_login,name="login"),
    path("logout",views.render_logout,name="logout"),
]
