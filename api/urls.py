from django.urls import path

from api.views import exchange_rates, CarouselListAPIView, CalculateLoanView

urlpatterns = [
    path('api/v1/exchange-rates/', exchange_rates, name='exchange-rates'),
    path('api/v1/calculate/', CalculateLoanView.as_view(), name='calculate_loan'),
    path('api/v1/carousels/', CarouselListAPIView.as_view(), name='carousel'),
]
