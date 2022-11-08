import io

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.customers.models import Customer
from apps.customers.serializers import CustomerSerializer
from cryptography.fernet import Fernet
import io


class Register(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):

        email = request.data['email']
        password = request.data['password']

        try:
            customer = Customer.objects.get(email=email)
            key = customer.key
            encrypted_password = customer.password

            if password == CustomerSerializer.decrypt_password(self, key, encrypted_password):
                customer.is_logged = True
                customer.save()
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)

            else:
                return Response({'message': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)

        except Customer.DoesNotExist:
            return Response({'message': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    def post(self, request):
        email = request.data['email']
        try:
            customer = Customer.objects.get(email=email)
            customer.is_logged = False
            customer.save()
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({'message': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)
