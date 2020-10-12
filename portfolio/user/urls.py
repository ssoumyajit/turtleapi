from django.urls import path
from rest_framework import generics
from .views import CreateUserView, CreateTokenView, ManageUserView

app_name = 'user'
#for using django reverse() function, it is a django utility function
# https://docs.djangoproject.com/en/3.0/ref/urlresolvers/

urlpatterns = [
    path('create/', CreateUserView.as_view(), name = 'create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('me/', ManageUserView.as_view(), name='me')
]