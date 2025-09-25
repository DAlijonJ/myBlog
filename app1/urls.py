from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("home", index, name="home"),
    path("login", sign_in, name='login'),
    path("post", post, name="post"),
    path("register", register, name="register"),
    path("author", filter_author, name="author")
]






