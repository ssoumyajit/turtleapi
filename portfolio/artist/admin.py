from django.contrib import admin

# Register your models here.
from .models import Artist, Gallery
admin.site.register(Artist)
admin.site.register(Gallery)
