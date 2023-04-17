from modeltranslation.translator import TranslationOptions, register
from .models import LegalEntitiesModel


@register(LegalEntitiesModel)
class LegalEntitiesModelTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description')
