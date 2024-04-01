from rest_framework import serializers
from .models import InventoryTracker


class InventoryTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTracker
        fields = ["name", "url", "count"]
