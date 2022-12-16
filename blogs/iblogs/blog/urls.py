from django.urls import path, include
from .views import home, post, about, category

urlpatterns = [
    path("", home),
    path("about/", about),
    path("blog/<slug:url>", post),
    path("category/<slug:url>", category),
]