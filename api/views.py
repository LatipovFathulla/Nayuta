from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response


# Exchange rates in home page
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