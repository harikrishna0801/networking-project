from django.urls import path
from .views import receive_device

urlpatterns = [
    path('device/', receive_device, name='receive_device'),
]
