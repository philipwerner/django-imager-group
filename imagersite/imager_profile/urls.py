"""."""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from imager_profile.views import ProfileView, UserView

urlpatterns = [
    url(r'^$',
        UserView.as_view(template_name='imager_profile/profile.html'),
        name='profile'),
    url(r'^(?P<username>\w+)/$',
        ProfileView.as_view(template_name='imager_profile/user_profile.html'),
        name='user_profile')
]