from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistListCreateViews, ArtistRetrieveUpdateDestroyViews, ArtistDataCreateViews, ArtistDataRetrieveUpdateDestroyViews
from rest_framework.urlpatterns import format_suffix_patterns

# app_name = 'artist'

urlpatterns = [
    path('portfolios/', ArtistListCreateViews.as_view()),
    path('portfolios/<int:pk>/', ArtistRetrieveUpdateDestroyViews.as_view()),
    path('bios/', ArtistDataCreateViews.as_view()),
    path('bios/<int:pk>/', ArtistDataRetrieveUpdateDestroyViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)




"""
router = DefaultRouter()

router.register('portfolio', ArtistViewSets)
router.register('portfoliodata', ArtistDataViewSets)
router.register('highlights', HighlightsViewSets)
router.register('events', EventsViewSets)

app_name = 'artist'

urlpatterns = [
    path(r'', include(router.urls)),
]
"""
