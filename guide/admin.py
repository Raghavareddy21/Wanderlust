from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Audio)
admin.site.register(models.Place)
admin.site.register(models.AudioRating)
admin.site.register(models.PlaceRating)
