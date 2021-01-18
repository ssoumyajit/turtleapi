from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BioViewSets, ArtistViewSets, GalleryViewSets, HighlightsViewSets, EventsViewSets, JudgingWorkshopViewSets

router = DefaultRouter()

# artist
router.register('portfolio', ArtistViewSets)
# bio
router.register('bio', BioViewSets)
# gallery
router.register('gallery', GalleryViewSets)
# highlights
router.register('highlights', HighlightsViewSets)
# jw
router.register('jw', JudgingWorkshopViewSets)
# events
router.register('events', EventsViewSets)

app_name = 'artist'

urlpatterns = [
    path(r'', include(router.urls)),
]
