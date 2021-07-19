"""Posts forms."""

# Django
from django import forms

# Models
from posts.models import Posts

class PostForm(forms.ModelForm):
    """Posts model form."""

    class Meta:
        """Form settings."""
        model = Posts
        fields = ('user', 'profile', 'title', 'photo')
