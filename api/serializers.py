from rest_framework import serializers

from api.models import CarouselModel, CalculatorModel, ProductModel, FAQModel, WhoseCreditModel, IndividualCreditModel, \
    IndividualCreditTypeModel


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
