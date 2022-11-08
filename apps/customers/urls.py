from django.urls import path
from .register import Register, Login, Logout
from .views import CustomerList, CustomerDetail

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('customers/', CustomerList.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer_detail'),
]
