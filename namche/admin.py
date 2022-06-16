from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=['name','image','price','capacity']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=['name','email','position']

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display=['name','image','price','type','category']

admin.site.register(Booking)