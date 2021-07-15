"""Users views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User

# Forms
from users.forms import SignupForm

class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""
    template_name = 'users/detail.html'


class SignupView(FormView):
    """Users signup view."""
    template_name = 'users/signup.html'
    form_class = SignupForm



class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'


class LoginView(auth_views.LoginView):
    """Login view."""
    Template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/logged_out.html'
