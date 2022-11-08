from django.urls import path
from .views import SheduleList

urlpatterns = [
    path('shedule/<int:customer_id>/<int:order_id>/', SheduleList.as_view()),
]
