from django.contrib import admin
from .models import Picture, Request, PictureGroup, PictureGroupUsers
# Register your models here.

admin.site.register(Picture)
admin.site.register(Request)
admin.site.register(PictureGroup)
admin.site.register(PictureGroupUsers)