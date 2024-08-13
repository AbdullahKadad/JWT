from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'price', 'is_bought')
    list_filter = ('brand', 'is_bought')
    search_fields = ('model', 'brand')
