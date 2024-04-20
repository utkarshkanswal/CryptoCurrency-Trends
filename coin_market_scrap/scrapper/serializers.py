from rest_framework import serializers
from .models import ScrappedData
class ScrappedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrappedData
        fields = ["Name", "Price", "one_hr", "twenty_four_hr", "seven_days_hr","market_cap","volume","circulating_supply","timestamp"]