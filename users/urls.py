"""Users URLs."""

# Django
from django.urls import path

# View
from users import views

urlpatterns = [
    
    path(
        route='login/',
        view=views.LoginView,
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView,
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SignupView,
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.UpdateProfileView,
        name='update'
    ),
    # Posts
    path(
        route='<str:username>',
        view=views.UserDetailView,
        name='detail'
    ),
]
