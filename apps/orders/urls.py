from django.urls import path
from .views import OrderList, OrderDetail, OrderLocation
from .filter import OrderListByDriver, OrderListByDateAndDriver

urlpatterns = [
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
    path('orders/<int:pk>/location/', OrderLocation.as_view()),
    path('orders/driver/<int:id>/', OrderListByDriver.as_view()),
    path('orders/driver/', OrderListByDateAndDriver.as_view()),

]

