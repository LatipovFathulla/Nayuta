from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin

from api.models import CarouselModel, ProductModel, FAQModel, \
    IndividualCreditTypeModel, LegalEntitiesModel, IndividualCreditModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


# Carousel administration
@admin.register(CarouselModel)
class CarouselModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title', 'med_image_tag', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at', 'updated_at']
    order_by = 'created_at'

    def med_image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="60" />'.format(obj.image.url))
        else:
            return '-'

    med_image_tag.short_description = 'Изображения'

# Calculator administration


@admin.register(ProductModel)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title', 'image_tag', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at', 'updated_at']
    ordering = ['-created_at']
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return format_html('<img src="{}" height="60" />'.format(obj.image.url))

    image_tag.short_description = 'Image'


@admin.register(FAQModel)
class FAQModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at', 'updated_at']
    ordering = ['-created_at']


# Fiz Admin
@admin.register(IndividualCreditModel)
class IndividualCreditModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title']
    ordering = ['-created_at']


@admin.register(IndividualCreditTypeModel)
class IndividualCreditTypeModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title', 'med_image_tag', 'sec_image_tag', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at', 'updated_at']
    ordering = ['-created_at']

    def med_image_tag(self, obj):
        if obj.first_image:
            return format_html('<img src="{}" height="60" />'.format(obj.first_image.url))
        else:
            return '-'

    med_image_tag.short_description = 'Изображения1'

    def sec_image_tag(self, obj):
        if obj.second_image:
            return format_html('<img src="{}" height="60" />'.format(obj.second_image.url))
        else:
            return '-'

    sec_image_tag.short_description = 'Изображения2'


@admin.register(LegalEntitiesModel)
class LegalEntitiesModel(MyTranslationAdmin):
    list_display = ['id', 'title', 'med_image_tag', 'sec_image_tag', 'created_at', 'updated_at']
    search_fields = ['title']

    def med_image_tag(self, obj):
        if obj.first_image:
            return format_html('<img src="{}" height="60" />'.format(obj.first_image.url))
        else:
            return '-'

    med_image_tag.short_description = 'Изображения1'

    def sec_image_tag(self, obj):
        if obj.second_image:
            return format_html('<img src="{}" height="60" />'.format(obj.second_image.url))
        else:
            return '-'

    sec_image_tag.short_description = 'Изображения2'