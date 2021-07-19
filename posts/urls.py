"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path(
        route='',
        view=views.PostsFeedView,
        name='index'
    ),
    path(
        route='posts/new/',
        view=views.CreatePostView,
        name='create'
    ),
    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView,
        name='detail'
    )
]
