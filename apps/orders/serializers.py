from rest_framework import serializers
from .models import Order, Type_Order, Status_Order, LocationOrder
from apps.customers.serializers import CustomerSerializer
from apps.payment.serializers import PaymentSerializer
from apps.shedule.serializers import SheduleSerializer
from apps.drivers.serializers import DriverSerializer


class LocationOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationOrder
        fields = ('id', 'order', 'city', 'country', 'latitude', 'longitude')


class OrderSerializer(serializers.ModelSerializer):
    location = LocationOrderSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = instance.customer.name, instance.customer.phone, instance.customer.email
        response['status'] = instance.status.name
        response['type_order'] = instance.type_order.name
        # response['payment'] = PaymentSerializer(instance.payment).data
        response['shedule'] = instance.shedule.collection_date, instance.shedule.collection_time
        response['driver'] = DriverSerializer(instance.driver).data
        return response

    def validate(self, data):
        if Order.objects.filter(customer=data['customer'], status__name='Pending'):
            raise serializers.ValidationError('El cliente tiene un pedido pendiente')
        return data

    def validate_customer(self, value):
        if not value.is_logged:
            raise serializers.ValidationError('El cliente no esta logueado')
        return value

