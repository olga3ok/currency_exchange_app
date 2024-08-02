# from django import forms
# import requests
#
# response = requests.get(url="https://v6.exchangerate-api.com/v6/c75344bfaede2383a752245a/latest/USD").json()
# currencies = response.get('conversion_rates')
#
#
# class ExchangeFrom(forms.Form):
#     amount = forms.FloatField(min_value=0.1,
#                               label="Сумма")
#     form_curr = forms.ModelChoiceField(queryset=currencies,
#                                   label="Отдаю")
#     to_curr = forms.ChoiceField(choices=((1, "1"), (2, "2"), (3, "3")),
#                                 label="Получаю")
#
#     amount.widget.attrs.update({"class":"text-center"})
#     form_curr.widget.attrs.update({"class":"form-select"})
#     to_curr.widget.attrs.update({"class":"form-select"})

