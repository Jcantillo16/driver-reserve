from django.urls import path
from .views import DriverList, DriverDetail, Locationdrivers

urlpatterns = [
    path('drivers/', DriverList.as_view()),
    path('drivers/<int:pk>/', DriverDetail.as_view()),
    path('drivers/location/', Locationdrivers.as_view()),
]
