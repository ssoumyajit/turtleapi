from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateArtistView, ArtistView

from artist import views

router = DefaultRouter()
router.register('artist', CreateArtistView, base_name='ArtistCreate')
router.register('xyz', ArtistView)

app_name = 'artist'

urlpatterns = [
    path("", include(router.urls)),
    path(r'create/artist/', CreateArtistView.as_view(), name = 'create_artist'),
    
]