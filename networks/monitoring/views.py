from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Device
from .serializers import DeviceSerializer


def home(request):
    return JsonResponse({
        "status": "Server is running",
        "endpoints": {
            "admin": "/admin/",
            "device_api": "/api/device/ (POST only)",
        },
    })


@api_view(['POST'])
def receive_device(request):
    serializer = DeviceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Data received successfully"})

    return Response(serializer.errors, status=400)
