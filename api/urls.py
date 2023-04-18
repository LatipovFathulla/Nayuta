from django.urls import path

from api.views import exchange_rates, CarouselListAPIView, CalculateLoanView, ProductSerializerListAPIView, \
    CalculatorListAPIView, FAQSerializerListAPIView, \
    IndividualCreditTypeModelSerializerListAPIVIew, \
    LegalEntitiesModelSerializerListAPIView, IndividualCreditModelSerializerListAPIView

urlpatterns = [
    path('api/v1/exchange-rates/', exchange_rates, name='exchange-rates'),
    path('api/v1/calculate/', CalculateLoanView.as_view(), name='calculate_loan'),
    path('api/v1/calculate-list/', CalculatorListAPIView.as_view(), name='calculate'),
    path('api/v1/carousels/', CarouselListAPIView.as_view(), name='carousel'),
    path('api/v1/products/', ProductSerializerListAPIView.as_view(), name='products'),
    path('api/v1/FAQ/', FAQSerializerListAPIView.as_view(), name='products'),
    path('api/v1/individual-credit/', IndividualCreditModelSerializerListAPIView.as_view(), name='individual-credit'),
    path('api/v1/individual-credit-type/', IndividualCreditTypeModelSerializerListAPIVIew.as_view(), name='individual-credit-type'),
    path('api/v1/legal-credit/', LegalEntitiesModelSerializerListAPIView.as_view(), name='legal-credit-type'),
]
