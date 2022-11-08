from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Order, LocationOrder, Type_Order, Status_Order
from .serializers import OrderSerializer, LocationOrderSerializer
from apps.drivers.views import Locationdrivers
from apps.drivers.models import Driver, LocationDriver
from apps.drivers.serializers import DriverSerializer

from geopy.distance import geodesic
from geopy import distance
from geopy import Point


class OrderList(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            location_order = LocationOrder.objects.create(order=serializer.instance)
            location_order.save()

            location_driver = Locationdrivers.get(self, request)
            location_driver = location_driver.data

            kms = []
            for i in location_driver['alfreds']:
                distance = geodesic((i['lat'], i['lng']), (location_order.latitude, location_order.longitude)).km
                if distance > 100:
                    distance = distance / 100
                    distance = round(distance, 2)
                kms.append(distance)

            min_distance = min(kms)
            index = kms.index(min_distance)
            driver = Driver.objects.get(id=location_driver['alfreds'][index]['id'])
            serializer_driver = DriverSerializer(driver)
            serializer.instance.driver = serializer_driver.instance
            serializer.instance.save()

            order = Order.objects.get(id=serializer.instance.id)
            order.driver = serializer_driver.instance
            order.save()

            driver = Driver.objects.get(id=serializer_driver.instance.id)
            driver.is_available = 0
            driver.save()

            order = Order.objects.get(id=serializer.instance.id)
            order.status = Status_Order.objects.get(name='In Progress')
            order.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    def get(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({
                "message": "Order Not Found"},
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            return Response({
                "message": "Order Not Found"},
                status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response({
                "message": "Order Not Found"},
                status=status.HTTP_404_NOT_FOUND)


class OrderLocation(APIView):
    def get(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
            location_order = LocationOrder.objects.get(order=order)
            serializer = LocationOrderSerializer(location_order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({
                "message": "Order Not Found"},
                status=status.HTTP_404_NOT_FOUND)
