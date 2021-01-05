from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from .views import CreateArtistView, UpdateArtistView, ArtistView, CreateGalleryView, GalleryView, WorkViewSets, ArtistViewSets
from .views import BioViewSets, ArtistViewSets, GalleryViewSets, HighlightsViewSets, EventsViewSets, JudgingWorkshopViewSets
from artist import views

router = DefaultRouter()

#artist
router.register('portfolio', ArtistViewSets)
#bio
router.register('bio', BioViewSets )
#gallery
router.register('gallery', GalleryViewSets)
#highlights
router.register('highlights', HighlightsViewSets)
#jw
router.register('jw', JudgingWorkshopViewSets)
#events
router.register('events', EventsViewSets)

'''
router.register('create', CreateArtistView, base_name='ArtistCreate')
router.register('list', ArtistView)
router.register('update', UpdateArtistView, base_name='ArtistUpdate')

#gallery
router.register('gallery/create', CreateArtistView, base_name='GalleryCreate')
router.register('gallery/list', GalleryView)

#work
router.register('work', WorkViewSets)
'''


app_name = 'artist'

urlpatterns = [
    path(r'', include(router.urls)),
    #path(r'create/', CreateArtistView.as_view({'get': 'list'}), name = 'create_artist'),
    
]