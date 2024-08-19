from django.shortcuts import render
from .utils import black_scholes

def option_price_view(request):
    if request.method == 'POST':
        option_type = request.POST.get('option_type')
        S = float(request.POST.get('stock_price'))
        K = float(request.POST.get('strike_price'))
        T = float(request.POST.get('time_to_maturity'))
        r = float(request.POST.get('risk_free_rate'))
        sigma = float(request.POST.get('volatility'))

        price = black_scholes(option_type, S, K, T, r, sigma)
        return render(request, 'pricing/result.html', {'price': price})

    return render(request, 'pricing/form.html')
