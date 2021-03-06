from django.shortcuts import render
from .models import Post


posts = [ 

    {
        "author": "Julio", 
        "title": "Blog Post 1", 
        "content": "First post content", 
        "date_posted": "April 12, 2021" 
    },

    {
        "author": "Jane", 
        "title": "Blog Post 2", 
        "content": "Second post content", 
        "date_posted": "April 12, 2021" 
    }





]

def home(request):
    
    context = {
        "posts": Post.objects.all() 
    }

    return render(request, "blog/home.html", context)

def about(request): 
    return render(request, "blog/about.html", {"title": "About"})