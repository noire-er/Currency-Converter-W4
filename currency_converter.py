def currency_converter(amount, from_currency, to_currency):
    
    conversion_rate = {
    'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
    'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
    'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
    'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }
    if amount < 0:
        return 0.0
    
    if from_currency == to_currency:
        return round(amount, 2)
    
    currencyRate = conversion_rate.get(from_currency, {}).get(to_currency)
    return round(amount * currencyRate, 2)