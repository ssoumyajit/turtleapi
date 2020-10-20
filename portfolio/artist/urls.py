from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateArtistView, ArtistView, CreateGalleryView, GalleryView

from artist import views

router = DefaultRouter()

#artist
router.register('create', CreateArtistView, base_name='ArtistCreate')
router.register('list', ArtistView)

#gallery
router.register('gallery/create', CreateArtistView, base_name='ArtistCreate')
router.register('gallery/list', ArtistView)


app_name = 'artist'

urlpatterns = [
    path(r'', include(router.urls)),
    #path(r'create/', CreateArtistView.as_view({'get': 'list'}), name = 'create_artist'),
    
]