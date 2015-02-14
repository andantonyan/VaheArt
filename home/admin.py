from django.contrib import admin
from .models import Section, Tag, GaleryImage, GaleryItem

admin.site.register(Section)
admin.site.register(Tag)
admin.site.register(GaleryImage)
admin.site.register(GaleryItem)
