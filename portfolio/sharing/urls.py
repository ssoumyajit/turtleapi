from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SharingViewSets

router = DefaultRouter()

#sharing
router.register('', SharingViewSets)

app_name = 'sharing'

urlpatterns = [
    path(r'', include(router.urls)),    
]
