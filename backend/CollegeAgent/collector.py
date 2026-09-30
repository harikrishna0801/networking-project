import socket
import uuid
import getpass
import psutil
import time

# Store previous network stats
previous = psutil.net_io_counters()
previous_time = time.time()


def get_connection_type():
    stats = psutil.net_if_stats()

    for name, value in stats.items():
        if value.isup:
            lname = name.lower()

            if "ethernet" in lname or "eth" in lname:
                return "Ethernet", name, value.speed

            if "wi-fi" in lname or "wifi" in lname or "wireless" in lname or "wlan" in lname:
                return "Wi-Fi", name, value.speed

    return "-", "-", 0


def get_data():
    global previous, previous_time

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    mac = ':'.join(
        ['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
         for ele in range(40, -1, -8)]
    )

    username = getpass.getuser()

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    connection_type, adapter_name, speed = get_connection_type()

    current = psutil.net_io_counters()
    current_time = time.time()

    elapsed = current_time - previous_time

    upload_speed = (current.bytes_sent - previous.bytes_sent) / elapsed
    download_speed = (current.bytes_recv - previous.bytes_recv) / elapsed

    previous = current
    previous_time = current_time

    return {
        "computer_name": hostname,
        "username": username,
        "ip_address": ip,
        "mac_address": mac,

        "connection_type": connection_type,
        "adapter_name": adapter_name,
        "link_speed": f"{speed} Mbps",

        "cpu_usage": cpu,
        "ram_usage": ram,

        # Required old fields
        "upload_bytes": current.bytes_sent,
        "download_bytes": current.bytes_recv,

        # New fields
        "upload_speed": round(upload_speed / 1024, 2),
        "download_speed": round(download_speed / 1024, 2),
        "total_upload": current.bytes_sent,
        "total_download": current.bytes_recv,

        "status": "Online"
    }