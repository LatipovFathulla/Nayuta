from modeltranslation.utils import get_language
from rest_framework import serializers

from api.models import CarouselModel, ProductModel, FAQModel, \
    IndividualCreditTypeModel, LegalEntitiesModel, IndividualCreditModel, Payment, Credit


# Carousel serializers
class CarouselModelSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    descriptions = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.title if get_language() == 'ru' else getattr(obj, f'title_{get_language()}')

    def get_descriptions(self, obj):
        return obj.descriptions if get_language() == 'ru' else getattr(obj, f'descriptions_{get_language()}')

    class Meta:
        model = CarouselModel
        fields = ['id', 'title', 'descriptions', 'image', 'link', 'created_at', 'updated_at']


# Calculator serializers
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'payment_number', 'payment_date', 'payment_amount', 'principal_amount', 'interest_amount',
            'remaining_balance')


class CreditSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True)
    total_payments = serializers.SerializerMethodField()
    overpayment = serializers.SerializerMethodField()

    class Meta:
        model = Credit
        fields = ('price', 'down_payment_percentage', 'loan_amount', 'interest_rate', 'payment_schedule', 'loan_period',
                  'payments', 'total_payments', 'overpayment')

    def get_total_payments(self, obj):
        payment_amount = obj.payments.first().payment_amount
        loan_period = obj.loan_period
        all = payment_amount * loan_period
        return all

    def get_overpayment(self, obj):
        total_payments = len(obj.payments.all())
        payment_amount = obj.payments.first().payment_amount
        total_amount = payment_amount * total_payments
        overpayment = total_amount - obj.loan_amount
        return str(overpayment)


# Product Serializers
class ProductSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.title if get_language() == 'ru' else getattr(obj, f'title_{get_language()}')

    def get_description(self, obj):
        return obj.description if get_language() == 'ru' else getattr(obj, f'description_{get_language()}')

    class Meta:
        model = ProductModel
        fields = ['id', 'image', 'title', 'description', 'link', 'created_at', 'updated_at']


# FAQs Serializers
class FAQSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.title if get_language() == 'ru' else getattr(obj, f'title_{get_language()}')

    def get_description(self, obj):
        return obj.description if get_language() == 'ru' else getattr(obj, f'description_{get_language()}')

    class Meta:
        model = FAQModel
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']


# Fiz Credit
class IndividualCreditModelSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.title if get_language() == 'ru' else getattr(obj, f'title_{get_language()}')

    def get_description(self, obj):
        return obj.description if get_language() == 'ru' else getattr(obj, f'description_{get_language()}')

    class Meta:
        model = IndividualCreditModel
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']


class IndividualCreditTypeModelSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.title if get_language() == 'ru' else getattr(obj, f'title_{get_language()}')

    def get_description(self, obj):
        return obj.description if get_language() == 'ru' else getattr(obj, f'description_{get_language()}')

    class Meta:
        model = IndividualCreditTypeModel
        fields = ['id', 'title', 'description', 'first_image', 'second_image', 'created_at', 'updated_at']


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
        return obj.title if get_language() == 'ru' else getattr(obj, f'title_{get_language()}')

    def get_short_description(self, obj):
        return obj.short_description if get_language() == 'ru' else getattr(obj, f'short_description_{get_language()}')

    def get_long_description(self, obj):
        return obj.long_description if get_language() == 'ru' else getattr(obj, f'long_description_{get_language()}')

    class Meta:
        model = LegalEntitiesModel
        fields = ['title', 'short_description', 'long_description']
