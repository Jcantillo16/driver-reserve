from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Order, LocationOrder, Type_Order, Status_Order
from .serializers import OrderSerializer, LocationOrderSerializer
from apps.drivers.views import Locationdrivers
from apps.drivers.models import Driver, LocationDriver
from apps.drivers.serializers import DriverSerializer

from apps.shedule.models import Shedule


class OrderListByDriver(APIView):
    def get(self, request, id):
        orders = Order.objects.filter(driver=id)
        serializer = OrderSerializer(orders, many=True)
        count = len(orders)
        return Response({'count': count,
                         'orders': serializer.data})


class OrderListByDateAndDriver(APIView):
    def get(self, request):
        date = request.GET.get('date')
        driver = request.GET.get('driver')
        if date and driver:
            orders = Order.objects.filter(shedule=Shedule.objects.get(collection_date=date), driver=driver)
            serializer = OrderSerializer(orders, many=True)
            count = len(orders)
            return Response({'count': count,
                             'orders': serializer.data})
        elif date:
            orders = Order.objects.filter(shedule=Shedule.objects.get(collection_date=date))
            serializer = OrderSerializer(orders, many=True)
            count = len(orders)
            return Response({'count': count,
                             'orders': serializer.data})

        elif driver:
            orders = Order.objects.filter(driver=driver)
            serializer = OrderSerializer(orders, many=True)
            count = len(orders)
            return Response({'count': count,
                             'orders': serializer.data})

        else:
            return Response({'error': 'Please provide Date or Driver'})
