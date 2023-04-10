from rest_framework import serializers

from api.models import CarouselModel, CalculatorModel


# Carousel serializers
class CarouselModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselModel
        fields = '__all__'


# Calculator serialziers
class CalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculatorModel
        fields = '__all__'
