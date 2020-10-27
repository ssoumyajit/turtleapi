from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateArtistView, UpdateArtistView, ArtistView, CreateGalleryView, GalleryView

from artist import views

router = DefaultRouter()

#artist
router.register('create', CreateArtistView, base_name='ArtistCreate')
router.register('list', ArtistView)
router.register('update', UpdateArtistView, base_name='ArtistUpdate')

#gallery
router.register('gallery/create', CreateArtistView, base_name='GalleryCreate')
router.register('gallery/list', GalleryView)



app_name = 'artist'

urlpatterns = [
    path(r'', include(router.urls)),
    #path(r'create/', CreateArtistView.as_view({'get': 'list'}), name = 'create_artist'),
    
]