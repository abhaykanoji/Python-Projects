from django.shortcuts import render
# from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def home(request):
    # load all the posts from db
    posts = Post.objects.all()[:11]
    print(posts)
    # print(posts)
    data = {
        "posts" : posts
    }

    return render(request, "home.html", data)

def post(request, url):
    post = Post.objects.get(url=url)
    # print(post)
    return render(request, "posts.html", {"post" : post})

def about(request):
    return render(request, "about.html")