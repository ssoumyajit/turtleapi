from django.shortcuts import render
from .models import Artist
from rest_framework import viewsets
from artist.serializers import ArtistSerializers, ArtistReadOnlySerializers, GalleryReadOnlySerializers, GallerySerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import filters
#from rest_framework.generics import CreateAPIView

#A viewset needs to inherit from viewsets.ViewSet.
class CreateArtistView(mixins.CreateModelMixin,viewsets.GenericViewSet):
    """
    create a new Artist Portfolio.
    """
    serializer_class = ArtistSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    #from CDRF.co, for later.
    '''
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save()
    '''


class UpdateArtistView(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    view to retrieve, update artist object.
    #RetrieveUpdateDestroyAPIView: we don't use it coz it is not inherited from viewsets rather views class.... be careful
    """
    serializer_class = ArtistSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    #def get_queryset(self):
        #return self.request.user.get(pk)

    #def get_object(self):
        #return self.request.user



class ArtistView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArtistReadOnlySerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['username__name']
    queryset = Artist.objects.all()
    #lookup_field = "name" #won't work because lookup_field field only works direct model attributes, not relationships.   

    '''
     def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def reverse_action(self, url_name, *args, **kwargs):
        """
        Reverse the action for the given `url_name`.
        """
        url_name = '%s-%s' % (self.basename, url_name)
        kwargs.setdefault('request', self.request)

        return reverse(url_name, *args, **kwargs)
    
    def get_queryset(self):
        pass
    '''

class GalleryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = GalleryReadOnlySerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['g_artist__name']
    queryset = Artist.objects.all()


class CreateGalleryView(mixins.CreateModelMixin,viewsets.GenericViewSet):
    """
    create a new Artist Portfolio.
    """
    serializer_class = GallerySerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

