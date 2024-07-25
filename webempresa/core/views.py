from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def store(request):
    return render(request, 'core/store.html')



def blog(request):
    return render(request, 'core/blog.html')

def home(request):
    posts = Post.objects.all()[:3]  # Ejemplo: Obtener los primeros 3 posts
    context = {
        'posts': posts,
    }
    return render(request, 'core/home.html', context)