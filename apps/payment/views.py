from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Payment, PaymentMethod
from .serializers import PaymentSerializer, PaymentMethodSerializer
from apps.customers.models import Customer
from apps.customers.serializers import CustomerSerializer


class PaymentMethodList(APIView):
    def get(self, request):
        payment_methods = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(payment_methods, many=True)
        return Response(serializer.data)


class PaymentMethodDetail(APIView):
    def get(self, request, pk):
        try:
            payment_method = PaymentMethod.objects.get(pk=pk)
            serializer = PaymentMethodSerializer(payment_method)
            return Response(serializer.data)
        except PaymentMethod.DoesNotExist:
            return Response(
                {"message": "Payment Method Not Found"},
                status=status.HTTP_404_NOT_FOUND)


class PaymentList(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetail(APIView):
    def get(self, request, pk):
        try:
            payment = Payment.objects.get(pk=pk)
            serializer = PaymentSerializer(payment)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response(
                {"message": "Payment Not Found"},
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            payment = Payment.objects.get(pk=pk)
            serializer = PaymentSerializer(payment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Payment.DoesNotExist:
            return Response(
                {"message": "Payment Not Found"},
                status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            payment = Payment.objects.get(pk=pk)
            payment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Payment.DoesNotExist:
            return Response(
                {"message": "Payment Not Found"},
                status=status.HTTP_404_NOT_FOUND)
