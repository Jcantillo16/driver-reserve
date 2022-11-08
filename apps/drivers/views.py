from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Driver, LocationDriver
from .serializers import DriverSerializer
from dotenv import load_dotenv
import os
import requests
import json
import datetime
import pytz

load_dotenv()


class DriverList(APIView):
    def get(self, request):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverDetail(APIView):
    def get(self, request, pk):
        try:
            driver = Driver.objects.get(pk=pk)
            serializer = DriverSerializer(driver)
            return Response(serializer.data)
        except Driver.DoesNotExist:
            return Response(
                {"messaje": "driver Not Found"},
                status=status.HTTP_404_NOT_FOUND)

    # TODO: SI SE REQUIERE UN CRUD COMPLETO PARA EL DRIVER...descomentar los metodos siguientes.

    # def put(self, request, pk):
    #     try:
    #         driver = Driver.objects.get(pk=pk)
    #         driver = DriverSerializer.update(driver, instance=driver, validated_data=request.data)
    #         serializer = DriverSerializer(driver)
    #         return Response(serializer.data)
    #     except Driver.DoesNotExist:
    #         return Response(
    #             {"messaje": "driver Not Found"},
    #             status=status.HTTP_404_NOT_FOUND)
    #
    # def delete(self, request, pk):
    #     try:
    #         driver = Driver.objects.get(pk=pk)
    #         driver.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     except Driver.DoesNotExist:
    #         return Response(
    #             {"messaje": "driver Not Found"},
    #             status=status.HTTP_404_NOT_FOUND)


class Locationdrivers(APIView):
    def get(self, request):
        url = os.getenv("LOCATION_DRIVERS")
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for driver in data['alfreds']:
                location_driver = LocationDriver.objects.create(
                    driver_id=driver['id'],
                    lat=driver['lat'],
                    lng=driver['lng'],
                    lastUpdate=driver['lastUpdate']
                )
                location_driver.save()

                # todo: si se quiere tener un registro de todas las ubicaciones de los drivers, comentar la linea siguiente
                LocationDriver.objects.filter(driver_id=driver['id']).exclude(id=location_driver.id).delete()

            return Response(data)
        else:
            return Response(
                {"messaje": "Error"},
                status=status.HTTP_404_NOT_FOUND
            )


