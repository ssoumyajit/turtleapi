from django.contrib import admin

# Register your models here.
from .models import Artist, Bio, Gallery, Highlights, JudgingWorkshop, Events
admin.site.register(Artist)
admin.site.register(Gallery)
admin.site.register(Bio)
admin.site.register(Highlights)
admin.site.register(JudgingWorkshop)
admin.site.register(Events)
