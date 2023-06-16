import os

from dateutil.relativedelta import relativedelta
from django.forms import model_to_dict
from django.utils.translation import activate
from rest_framework.decorators import api_view
import requests
from datetime import datetime, timedelta
from rest_framework import status

from bank import settings
from .models import Credit, Payment
from .serializers import CreditSerializer
from decimal import Decimal

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

# Exchange rates in home page
from api.models import CarouselModel, ProductModel, FAQModel, IndividualCreditTypeModel, \
    LegalEntitiesModel, IndividualCreditModel
from api.serializers import CarouselModelSerializer, ProductSerializer, FAQSerializer, \
    IndividualCreditTypeModelSerializer, \
    LegalEntitiesModelSerializer, IndividualCreditModelSerializer
from .utils import generate_pdf


@api_view(['GET'])
def exchange_rates(request):
    ''' Exchange rates(Dollar and much more)'''
    url = 'https://nbu.uz/uz/exchange-rates/json/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        filtered_data = {}
        for rate in data:
            if rate['code'] in ['EUR', 'JPY', 'RUB', 'USD']:
                filtered_data[rate['code']] = rate
        return Response(filtered_data)
    else:
        return Response(status=404)


# End exchange rates in home page

# Carousel method GET
class CarouselListAPIView(ListAPIView):
    ''' Carouse view'''
    queryset = CarouselModel.objects.all()
    serializer_class = CarouselModelSerializer

    def list(self, request, *args, **kwargs):
        language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        if language:
            activate(language)

        return super().list(request, *args, **kwargs)


#Calculate
# class CreditCalculatorAPIView(CreateAPIView):
#     serializer_class = CreditSerializer
#     queryset = Credit.objects.all()
#
#     def create(self, request, *args, **kwargs):
#         # Получаем данные из запроса
#         data = request.data
#
#         # Вычисляем параметры кредита
#         price = Decimal(data['price'])
#         down_payment_percentage = Decimal(data['down_payment_percentage'])
#         loan_amount = Decimal(data['loan_amount'])
#         interest_rate = Decimal(data['interest_rate']) / 100
#         payment_schedule = data['payment_schedule']
#         loan_period = int(data['loan_period'])
#
#         # Вычисляем параметры выплаты
#         if payment_schedule == 'annuity':
#             # Аннуитетный платеж
#             payment_amount = loan_amount * (interest_rate / 12) * ((1 + interest_rate / 12) ** (loan_period * 12)) / (((1 + interest_rate / 12) ** (loan_period * 12)) - 1)
#         elif payment_schedule == 'differentiated':
#             # Дифференцированный платеж
#             payment_amount = loan_amount / (loan_period * 12)
#
#         # Вычисляем даты и суммы платежей
#         payment_date = datetime.now().
#         remaining_balance = loan_amount
#         payments = []
#         for i in range(1, loan_period * 12 + 1):
#             if payment_schedule == 'annuity':
#                 # Аннуитетный платеж
#                 interest_amount = remaining_balance * (interest_rate / 12)
#                 principal_amount = payment_amount - interest_amount
#             elif payment_schedule == 'differentiated':
#                 # Дифференцированный платеж
#                 principal_amount = loan_amount / (loan_period * 12)
#                 interest_amount = remaining_balance * (interest_rate / 12)
#                 payment_amount = principal_amount + interest_amount
#
#             remaining_balance -= principal_amount
#
#             # Сохраняем данные платежа в модели Payment
#             payment = Payment(
#                 credit=None,
#                 payment_number=i,
#                 payment_date=payment_date,
#                 payment_amount=payment_amount,
#                 principal_amount=principal_amount,
#                 interest_amount=interest_amount,
#                 remaining_balance=remaining_balance
#             )
#             payments.append(payment)
#
#             if payment_schedule == 'annuity':
#                 # Добавляем месяц к дате следующего платежа
#                 payment_date += timedelta(days=30)
#
#         # Сохраняем данные кредита и платежей в базе данных
#         down_payment_amount = price * (down_payment_percentage / 100)
#         loan_amount = price - down_payment_amount
#         credit = Credit(
#             price=price,
#             down_payment_percentage=down_payment_percentage,
#             loan_amount=loan_amount,
#             interest_rate=interest_rate * 100,
#             payment_schedule=payment_schedule,
#             loan_period=loan_period
#         )
#         credit.save()
#         for payment in payments:
#             payment.credit = credit
#             payment.save()
#
#         # Возвращаем данные в ответе
#         serializer = CreditSerializer(credit)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreditCalculatorAPIView(CreateAPIView):
    serializer_class = CreditSerializer
    queryset = Credit.objects.all()

    def create(self, request, *args, **kwargs):
        # Получаем данные из запроса
        data = request.data

        # Вычисляем параметры кредита
        price = Decimal(data['price'])
        down_payment_percentage = Decimal(data['down_payment_percentage'])
        loan_amount = Decimal(data['loan_amount'])
        interest_rate = Decimal(data['interest_rate']) / 100
        payment_schedule = data['payment_schedule']
        loan_period = int(data['loan_period'])

        # Вычисляем параметры выплаты
        if payment_schedule == 'annuity':
            # Аннуитетный платеж
            payment_amount = loan_amount * (interest_rate / 12) * ((1 + interest_rate / 12) ** (loan_period)) / (((1 + interest_rate / 12) ** (loan_period)) - 1)
        elif payment_schedule == 'differentiated':
            # Дифференцированный платеж
            payment_amount = loan_amount / loan_period

        # Вычисляем даты и суммы платежей
        payment_date = datetime.now() + relativedelta(months=1)
        remaining_balance = loan_amount
        total_payments = 0
        overpayment = 0
        payments = []
        for i in range(1, loan_period + 1):
            if payment_schedule == 'annuity':
                # Аннуитетный платеж
                payment_amount = loan_amount * (interest_rate / 12) * ((1 + interest_rate / 12) ** (loan_period)) / (((1 + interest_rate / 12) ** (loan_period)) - 1)
                interest_amount = remaining_balance * (interest_rate / 12)
                principal_amount = payment_amount - interest_amount
            elif payment_schedule == 'differentiated':
                # Дифференцированный платеж
                principal_amount = loan_amount / loan_period
                interest_amount = remaining_balance * (interest_rate / 12)
                payment_amount = principal_amount + interest_amount
                overpayment += interest_amount

            total_payments += payment_amount
            remaining_balance -= principal_amount

            if payment_schedule == 'differentiated':
                overpayment += interest_amount

            # Сохраняем данные платежа в модели Payment
            payment = Payment(
                credit=None,
                payment_number=i,
                payment_date=payment_date,
                payment_amount=payment_amount,
                principal_amount=principal_amount,
                interest_amount=interest_amount,
                remaining_balance=remaining_balance
            )
            payments.append(payment)

            if payment_schedule == 'annuity':
                # Добавляем месяц к дате следующего платежа
                payment_date += relativedelta(months=1)
            elif payment_schedule == 'differentiated':
                payment_date += relativedelta(months=1)

        # Сохраняем данные кредита и платежей в базе данных
        down_payment_amount = price * (down_payment_percentage / 100)
        loan_amount = price - down_payment_amount
        credit = Credit(
            price=price,
            down_payment_percentage=down_payment_percentage,
            loan_amount=loan_amount,
            interest_rate=interest_rate * 100,
            payment_schedule=payment_schedule,
            loan_period=loan_period
        )
        credit.save()
        for payment in payments:
            payment.credit = credit
            payment.save()

        payment_data = [model_to_dict(payment) for payment in payments]

        pdf_filename = generate_pdf(
            payment_data,
            price,
            down_payment_percentage,
            loan_amount,
            interest_rate,
            payment_schedule,
            loan_period,
            total_payments,
        )
        # Возвращаем данные в ответе
        serializer = CreditSerializer(credit)
        response_data = serializer.data
        pdf_url = os.path.join(settings.MEDIA_URL, 'pdf', os.path.basename(pdf_filename))
        response_data['pdf'] = request.build_absolute_uri(pdf_url)
        return Response(response_data, status=status.HTTP_201_CREATED)

# Products serialziers
class ProductSerializerListAPIView(ListAPIView):
    ''' Products = Микрозайм, микрокредиты и т.д'''
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        if language:
            activate(language)

        return super().list(request, *args, **kwargs)
# FAQ serializers
class FAQSerializerListAPIView(ListAPIView):
    ''' FAQ = Часто задаваемые вопросы (GET) '''
    queryset = FAQModel.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        if language:
            activate(language)

        return super().list(request, *args, **kwargs)


# Fiz credit
class IndividualCreditModelSerializerListAPIView(ListAPIView):
    '''Физ лицам Кто может получать кредит ..'''
    queryset = IndividualCreditModel.objects.all()
    serializer_class = IndividualCreditModelSerializer

    def list(self, request, *args, **kwargs):
        language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        if language:
            activate(language)

        return super().list(request, *args, **kwargs)


class IndividualCreditTypeModelSerializerListAPIVIew(ListAPIView):
    '''Физ лицам Автокредит до 50 млн сум на 36 месяцев ....'''
    queryset = IndividualCreditTypeModel.objects.all()
    serializer_class = IndividualCreditTypeModelSerializer

    def list(self, request, *args, **kwargs):
        language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        if language:
            activate(language)

        return super().list(request, *args, **kwargs)


# class LegalEntitiesModelSerializerListAPIView(ListAPIView):
#     queryset = LegalEntitiesModel.objects.all()
#     serializer_class = LegalEntitiesModelSerializer

class LegalEntitiesModelSerializerListAPIView(ListAPIView):
    ''' Юр лицам Автокредит до 300 млн сумна 36 месяцев'''
    queryset = LegalEntitiesModel.objects.all()
    serializer_class = LegalEntitiesModelSerializer

    def list(self, request, *args, **kwargs):
        language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        if language:
            activate(language)

        return super().list(request, *args, **kwargs)
