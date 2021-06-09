from django.contrib import admin
from .models import Profile ,CriminalProfile
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

@admin.register(CriminalProfile)
class CriminalProfileAdmin(admin.ModelAdmin):
    list_display = ['Name', 'date_of_birth', 'photo']