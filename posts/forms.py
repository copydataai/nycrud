"""Posts forms."""

# Django
from django.forms import ModelForm

# Models
from posts.models import Posts

class PostForm(ModelForm):
    
    class Meta:
        post = Posts
        fields = []
