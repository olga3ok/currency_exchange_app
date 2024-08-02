from django.conf import settings
from django.shortcuts import render
import requests


url = f"https://v6.exchangerate-api.com/v6/{settings.SECRET_API}/latest/USD"


def exchange(request):
    response = requests.get(url=url).json()
    currencies = response.get('conversion_rates')

    if request.method == 'GET':
        data = {
            'currencies': currencies
        }
        return render(request, 'index.html', context=data)

    if request.method == "POST":
        amount = request.POST.get('amount')
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(amount), 2)

        data = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'amount': amount,
            'currencies': currencies,
            'converted_amount': converted_amount
        }

        return render(request, 'index.html', context=data)
