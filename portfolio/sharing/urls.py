from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SharingViewSets, CommentViewSets

router = DefaultRouter()

#sharing
router.register('sharing', SharingViewSets)
#comments
router.register('comments', CommentViewSets)

app_name = 'sharing'

urlpatterns = [
    path(r'', include(router.urls)),    
]
