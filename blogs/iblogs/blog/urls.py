from django.urls import path, include
from .views import home, post, about

urlpatterns = [
    path("", home),
    path("about/", about),
    path("blog/<slug:url>", post),
]