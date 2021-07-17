"""Users forms."""

# Django
from django.forms import ModelForm
from users.models import Profile


class SignupForm(ModelForm):

    class Meta:
        model = Profile
        fields = []
