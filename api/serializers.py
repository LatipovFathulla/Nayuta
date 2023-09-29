from modeltranslation.utils import get_language
from rest_framework import serializers

from api.models import CarouselModel, ProductModel, FAQModel, \
    IndividualCreditTypeModel, LegalEntitiesModel, IndividualCreditModel, Payment, Credit, JapaneseCarouselModel, \
    JapaneseProductModel, JapaneseTeamModel, JapanesePDF


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
        fields = ['id', 'title', 'descriptions', 'image', 'created_at', 'updated_at']


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
    pdf = serializers.SerializerMethodField()

    class Meta:
        model = Credit
        fields = ('price', 'down_payment_percentage', 'loan_amount', 'interest_rate', 'payment_schedule', 'loan_period',
                  'payments', 'total_payments', 'overpayment', 'pdf')
        read_only_fields = ['pdf']

    def get_pdf(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.pdf)
        return None

    def get_total_payments(self, obj):
        if obj.payment_schedule == 'annuity':
            payment_amount = obj.payments.first().payment_amount
            loan_period = obj.loan_period
            total_payments = payment_amount * loan_period
        elif obj.payment_schedule == 'differentiated':
            total_payments = sum(payment.payment_amount + 5600 for payment in obj.payments.all())
        else:
            total_payments = 0
        return '{:,.2f}'.format(total_payments)

    def get_overpayment(self, obj):
        if obj.payment_schedule == 'annuity':
            total_payments = obj.loan_period
            payment_amount = obj.payments.first().payment_amount
            total_amount = payment_amount * total_payments
            overpayment = total_amount - obj.loan_amount
        elif obj.payment_schedule == 'differentiated':
            total_payments = sum(payment.payment_amount + 300 for payment in obj.payments.all())
            overpayment = total_payments - obj.loan_amount
        else:
            overpayment = 0
        return '{:,.2f}'.format(overpayment)


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
        fields = ['title', 'short_description', 'long_description', 'first_image', 'second_image']


class JapaneseCarouselModelSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    descriptions = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.title if get_language() == 'ru' else getattr(obj, f'title_{get_language()}')

    def get_descriptions(self, obj):
        return obj.descriptions if get_language() == 'ru' else getattr(obj, f'descriptions_{get_language()}')

    class Meta:
        model = JapaneseCarouselModel
        fields = ['title', 'descriptions', 'image', 'created_at', 'updated_at']


class JapaneseProductModelSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.title if get_language() == 'ru' else getattr(obj, f'title_{get_language()}')

    def get_description(self, obj):
        return obj.description if get_language() == 'ru' else getattr(obj, f'description_{get_language()}')

    class Meta:
        model = JapaneseProductModel
        fields = ['title', 'description', 'image', 'created_at', 'updated_at']


class JapaneseTeamModelSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name if get_language() == 'ru' else getattr(obj, f'name_{get_language()}')

    def get_description(self, obj):
        return obj.description if get_language() == 'ru' else getattr(obj, f'description_{get_language()}')

    class Meta:
        model = JapaneseTeamModel
        fields = ['name', 'description', 'image', 'created_at', 'updated_at']


class JapanesePDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = JapanesePDF
        fields = '__all__'
