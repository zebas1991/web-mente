from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from django.views.generic import ListView, DetailView

class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

def category(request, category_id):
    category = get_object_or_404(Category, id= category_id)
    posts = category.get_posts.all()
    return render(request, 'blog/category.html', {'category': category, 'posts':posts})