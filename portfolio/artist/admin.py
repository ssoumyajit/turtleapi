from django.contrib import admin

# Register your models here.
from .models import Artist, ArtistData, Highlights, Journey
admin.site.register(Artist)
admin.site.register(ArtistData)
admin.site.register(Highlights)
admin.site.register(Journey)
