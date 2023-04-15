from rest_framework.decorators import api_view
import requests
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

# Exchange rates in home page
from api.models import CarouselModel, ProductModel, CalculatorModel, FAQModel, IndividualCreditTypeModel, \
    WhoseCreditModel, IndividualCreditModel
from api.serializers import CarouselModelSerializer, CalculatorSerializer, ProductSerializer, FAQSerializer, \
    WhoseCreditModelSerializer, IndividualCreditModelSerializer, IndividualCreditTypeModelSerializer


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


# Calcularor method
class CalculatorListAPIView(ListAPIView):
    ''' Calcularor view (GET)'''
    queryset = CalculatorModel.objects.all()
    serializer_class = CalculatorSerializer


class CalculateLoanView(CreateAPIView):
    ''' Calcularor view (POST)'''
    serializer_class = CalculatorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Расчет ежемесячного платежа по кредиту
        n = serializer.validated_data['loan_term']
        r = (serializer.validated_data['interest_rate'] / 100) / 12
        p = serializer.validated_data['loan_amount']
        if r == 0:
            monthly_payment = p / n
        else:
            monthly_payment = p * r * ((1 + r) ** n) / (((1 + r) ** n) - 1)

        # Возвращаем результат в формате JSON
        response_data = serializer.validated_data
        response_data['monthly_payment'] = round(monthly_payment, 2)
        return Response(response_data)


# Products serialziers
class ProductSerializerListAPIView(ListAPIView):
    ''' Products = Микрозайм, микрокредиты и т.д'''
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


# FAQ serializers
class FAQSerializerListAPIView(ListAPIView):
    ''' FAQ = Часто задаваемые вопросы (GET) '''
    queryset = FAQModel.objects.all()
    serializer_class = FAQSerializer


# Fiz credit
class WhoseCreditModelSerializerListAPIVIew(ListAPIView):
    queryset = WhoseCreditModel.objects.all()
    serializer_class = WhoseCreditModelSerializer


class IndividualCreditModelSerializerListAPIVIew(ListAPIView):
    queryset = IndividualCreditModel.objects.all()
    serializer_class = IndividualCreditModelSerializer


class IndividualCreditTypeModelSerializerListAPIVIew(ListAPIView):
    queryset = IndividualCreditTypeModel.objects.all()
    serializer_class = IndividualCreditTypeModelSerializer
