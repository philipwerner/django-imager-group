"""."""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from imager_profile.views import ProfileView, UserView, EditProfileView, AddImage, AddAlbum

urlpatterns = [
    url(r'^$',
        UserView.as_view(template_name='imager_profile/user_profile.html'),
        name='profile'),
    url(r'^edit/$',
        EditProfileView.as_view(template_name='imager_profile/edit_profile.html'),
        name='edit_profile'),
    url(r'^add_image$',
        AddImage.as_view(template_name='imager_profile/add_image.html'),
        name='add_image'),
    url(r'^add_album/$',
        AddAlbum.as_view(template_name='imager_profile/add_album.html'),
        name='add_album'),

]
