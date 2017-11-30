"""."""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from imager_profile import views

urlpatterns = [
    url(r'^$', views.profile_view, name='user_profile'),
    url(r'^(?P<username>\w+)', views.profile_view, name='profile'),
]