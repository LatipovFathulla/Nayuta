from django.contrib import admin

from api.models import CarouselModel, CalculatorModel


# Carousel administration
@admin.register(CarouselModel)
class CarouselModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at', 'updated_at']
    order_by = 'created_at'


@admin.register(CalculatorModel)
class CalculatorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'borrower_type', 'loan_amount', 'loan_term']
    search_fields = ['id']
