from rest_framework import serializers
from .models import PaymentMethod, Payment
from apps.customers.serializers import CustomerSerializer


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    payment_method = PaymentMethodSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'
