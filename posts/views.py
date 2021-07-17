"""Posts views."""

# Django
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

# Forms
from posts.forms import PostForm

# Models 
from posts.models import Posts

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    template_name = 'posts/index.html'
    model = Posts

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""
    template_name = 'posts/detail.html'
    queryset = Posts.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""
    template_name = 'posts/new.html'
    form_class = PostForm
