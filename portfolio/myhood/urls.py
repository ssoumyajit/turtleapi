from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myhood.views import MyHoodViewSets, StudentsViewSets, PostViewSets

router = DefaultRouter()

#myhood
router.register('myhood', MyHoodViewSets)
#students
router.register('students', StudentsViewSets)
#post
router.register('posts', PostViewSets)

app_name = 'myhood'

urlpatterns = [
    path(r'', include(router.urls)),
        
]