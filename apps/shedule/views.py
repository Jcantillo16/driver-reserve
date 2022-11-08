from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Shedule
from .serializers import SheduleSerializer
from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer
from apps.customers.models import Customer
from apps.customers.serializers import CustomerSerializer


class SheduleList(APIView):
    def get(self, request):
        shedule = Shedule.objects.all()
        serializer = SheduleSerializer(shedule, many=True)
        return Response(serializer.data)

    def post(self, request, customer_id, order_id):
        customer = Customer.objects.get(id=customer_id)

        if customer.is_logged:
            serializer = SheduleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                order = Order.objects.get(id=order_id)
                order.shedule = serializer.instance
                order.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class SheduleDetail(APIView):
    def get(self, request, pk):
        try:
            shedule = Shedule.objects.get(pk=pk)
            serializer = SheduleSerializer(shedule)
            return Response(serializer.data)
        except Shedule.DoesNotExist:
            return Response({
                "message": "The shedule does not exist"},
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            shedule = Shedule.objects.get(pk=pk)
            serializer = SheduleSerializer(shedule, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Shedule.DoesNotExist:
            return Response({
                "message": "The shedule does not exist"},
                status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            shedule = Shedule.objects.get(pk=pk)
            shedule.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Shedule.DoesNotExist:
            return Response({
                "message": "The shedule does not exist"},
                status=status.HTTP_404_NOT_FOUND)
