from modeltranslation.utils import get_language
from rest_framework import serializers

from api.models import CarouselModel, CalculatorModel, ProductModel, FAQModel, WhoseCreditModel, IndividualCreditModel, \
    IndividualCreditTypeModel, LegalEntitiesModel


# Carousel serializers
class CarouselModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselModel
        fields = '__all__'


# Calculator serializers
class CalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculatorModel
        fields = '__all__'


# Product Serializers
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


# FAQs Serializers
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQModel
        fields = '__all__'


# Fiz Credit
class WhoseCreditModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoseCreditModel
        fields = '__all__'


class IndividualCreditModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualCreditModel
        fields = '__all__'


class IndividualCreditTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualCreditTypeModel
        fields = '__all__'


# Yuridik credit
# class LegalEntitiesModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LegalEntitiesModel
#         fields = '__all__'

class LegalEntitiesModelSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()
    long_description = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.title if get_language() == 'en' else getattr(obj, f'title_{get_language()}')

    def get_short_description(self, obj):
        return obj.short_description if get_language() == 'en' else getattr(obj, f'short_description_{get_language()}')

    def get_long_description(self, obj):
        return obj.long_description if get_language() == 'en' else getattr(obj, f'long_description_{get_language()}')

    class Meta:
        model = LegalEntitiesModel
        fields = ['title', 'short_description', 'long_description']
