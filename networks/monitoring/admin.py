from django.contrib import admin
from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        "computer_name", "username", "ip_address", "cpu_usage",
        "ram_usage", "status", "last_seen",
    )
