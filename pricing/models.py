from django.db import models

class Option(models.Model):
    option_type = models.CharField(max_length=4, choices=[('call', 'Call'), ('put', 'Put')])
    strike_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_price = models.DecimalField(max_digits=10, decimal_places=2)
    volatility = models.DecimalField(max_digits=5, decimal_places=2)
    time_to_maturity = models.DecimalField(max_digits=5, decimal_places=4)
    risk_free_rate = models.DecimalField(max_digits=4, decimal_places=3)

    def __str__(self):
        return f"{self.option_type.capitalize()} Option with Strike Price {self.strike_price}"
