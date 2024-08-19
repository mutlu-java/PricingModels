from django.urls import path
from .views import option_price_view

urlpatterns = [
    path('price/', option_price_view, name='option_price'),
]
