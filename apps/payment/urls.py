from django.urls import path
from .views import PaymentList, PaymentMethodList, PaymentDetail, PaymentMethodDetail

urlpatterns = [

    path('payments/', PaymentList.as_view()),
    path('payment-methods/', PaymentMethodList.as_view()),
    path('payments/<int:pk>/', PaymentDetail.as_view()),
    path('payment-methods/<int:pk>/', PaymentMethodDetail.as_view()),
]
