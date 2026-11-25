from django.db import models
from django.contrib import admin

class Restaurant(models.Model):
    rid = models.IntegerField()
    rname = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField()

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('rid', 'rname', 'location', 'cuisine', 'rating')