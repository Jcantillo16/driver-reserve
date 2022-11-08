from rest_framework import serializers
from .models import Shedule
from apps.orders.models import Order


class SheduleSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = Shedule
        fields = '__all__'

    def validate_collection_time(self, value):
        if value.hour < 8 or value.hour > 17:
            raise serializers.ValidationError("The time should be between 8:00 and 17:00.")
        return value

    def validate_collection_date(self, value):
        if value.weekday() > 4:
            raise serializers.ValidationError("The date should be between Monday and Friday.")
        return value
