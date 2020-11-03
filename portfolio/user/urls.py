from django.urls import path
from rest_framework import generics
from .views import CreateUserView, CreateTokenView, ManageUserView, CustomObtainAuthToken

app_name = 'user'
#for using django reverse() function, it is a django utility function
# https://docs.djangoproject.com/en/3.0/ref/urlresolvers/

urlpatterns = [
    path('auth/', CustomObtainAuthToken.as_view()),
    path('create/', CreateUserView.as_view(), name = 'create'),
    path('login/', CreateTokenView.as_view(), name='login'),
    path('update/', ManageUserView.as_view(), name='update')
]