from django.db import models


class Device(models.Model):
    computer_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=50)
    cpu_usage = models.FloatField()
    ram_usage = models.FloatField()
    upload_bytes = models.BigIntegerField()
    download_bytes = models.BigIntegerField()
    status = models.CharField(max_length=20, default="Online")
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.computer_name
