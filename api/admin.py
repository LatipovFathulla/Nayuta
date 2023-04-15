from django.contrib import admin
from django.utils.html import format_html

from api.models import CarouselModel, CalculatorModel, ProductModel, FAQModel, WhoseCreditModel, IndividualCreditModel, \
    IndividualCreditTypeModel, LegalEntitiesModel


# Carousel administration
@admin.register(CarouselModel)
class CarouselModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at', 'updated_at']
    order_by = 'created_at'


# Calculator administration
@admin.register(CalculatorModel)
class CalculatorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'borrower_type', 'loan_amount', 'loan_term']
    search_fields = ['id']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image_tag', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at', 'updated_at']
    ordering = ['-created_at']
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return format_html('<img src="{}" height="60" />'.format(obj.image.url))

    image_tag.short_description = 'Image'


@admin.register(FAQModel)
class FAQModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at', 'updated_at']
    ordering = ['-created_at']


# Fiz Admin
@admin.register(WhoseCreditModel)
class WhoseCreditModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at', 'updated_at']
    ordering = ['-created_at']


@admin.register(IndividualCreditModel)
class IndividualCreditModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at', 'updated_at']
    ordering = ['-created_at']


@admin.register(IndividualCreditTypeModel)
class IndividualCreditTypeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at', 'updated_at']
    ordering = ['-created_at']


@admin.register(LegalEntitiesModel)
class LegalEntitiesModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title']
