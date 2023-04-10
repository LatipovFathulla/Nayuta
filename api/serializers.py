from rest_framework import serializers

from api.models import CarouselModel


class CarouselModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselModel
        fields = '__all__'
