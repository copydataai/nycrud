"""Posts views."""

# Django
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Forms
from posts.forms import PostForm

# Models 
from posts.models import Post

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    template_name = 'posts/index.html'
    model = Post
