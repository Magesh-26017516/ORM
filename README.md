# Ex02 Django ORM Web Application
## Register no: 26017516
## Date: 25-11-2026

## AIM

To develop a Django application to store and retrieve restaurant data from an online food delivery platform database like Zomato or Swiggy using Object Relational Mapping (ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
~~~
#Admin.py
from django.contrib import admin
from .models import Restaurant, RestaurantAdmin

admin.site.register(Restaurant, RestaurantAdmin)
~~~
~~~
#model.py
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
~~~


## OUTPUT
![alt text](<Screenshot 2026-11-25 161246.jpg>)

![alt text](<Screenshot 2026-11-25 161324.jpg>)
## RESULT
Thus, the Django application for creating, storing and retrieving restaurant data from an online food delivery platform database using Object Relational Mapping (ORM) has been executed successfully.