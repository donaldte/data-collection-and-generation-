from django.contrib import admin
from .models import UserProfile

# Register your models here.
class AdminProfile(admin.ModelAdmin):
    list_display = ("identification",  "Born_year")

admin.site.register(UserProfile, AdminProfile)    