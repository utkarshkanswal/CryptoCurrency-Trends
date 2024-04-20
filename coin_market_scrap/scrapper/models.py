from django.db import models
from django.contrib import admin

class ScrappedData(models.Model):
    Name = models.CharField(max_length=200, default='NONE',null=False, blank=False)
    Price = models.CharField(max_length=200, default='NONE')
    one_hr = models.CharField(max_length=200, default='NONE')
    twenty_four_hr = models.CharField(max_length=200, default='NONE')
    seven_days_hr = models.CharField(max_length=200, default='NONE')
    market_cap = models.CharField(max_length=200, default='NONE')
    volume = models.CharField(max_length=200, default='NONE')
    circulating_supply = models.CharField(max_length=200, default='NONE')

    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self) -> str:
        return f"{self.Name}"

admin.site.register(ScrappedData)

