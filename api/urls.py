from django.urls import path

from api.views import exchange_rates

urlpatterns = [
    path('api/v1/exchange-rates/', exchange_rates, name='exchange-rates')
]
