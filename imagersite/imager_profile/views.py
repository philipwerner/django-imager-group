
"""Django imager views."""
from django.shortcuts import render


def home_view(request, number=None):
    """View for the home page."""
    return render(request, 'imagersite/home.html')


# def login_view(request):
#     """View for the login page."""
#     return render(request, 'imagersite/login.html')

def profile_view(request):
    """View for the profile view."""
    return render(request, 'imagersite/profile.html')