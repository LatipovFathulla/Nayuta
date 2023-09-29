from modeltranslation.translator import TranslationOptions, register
from .models import LegalEntitiesModel, CarouselModel, ProductModel, FAQModel, IndividualCreditModel, \
    IndividualCreditTypeModel, JapaneseCarouselModel, JapaneseProductModel, JapaneseTeamModel, JapanesePDF


@register(LegalEntitiesModel)
class LegalEntitiesModelTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description')


@register(CarouselModel)
class CarouselModelTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')


@register(ProductModel)
class CarouselModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(FAQModel)
class CarouselModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(IndividualCreditModel)
class CarouselModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(IndividualCreditTypeModel)
class CarouselModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(JapaneseCarouselModel)
class JapaneseCarouselModelTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')


@register(JapaneseProductModel)
class JapaneseProductModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(JapaneseTeamModel)
class JapaneseTeamModelTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

