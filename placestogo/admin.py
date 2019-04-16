from django.contrib import admin
from .models import Place

# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Place, PlaceAdmin)