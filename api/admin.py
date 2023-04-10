from django.contrib import admin

# Carousel administration
from api.models import CarouselModel


@admin.register(CarouselModel)
class CarouselModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at', 'updated_at']
    order_by = 'created_at'
