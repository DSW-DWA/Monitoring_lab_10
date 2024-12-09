from prometheus_client import start_http_server, Gauge
import psutil
import os
import time
from dotenv import load_dotenv

cpu_usage = Gauge('cpu_usage', 'CPU Usage per core', ['core'])
memory_total = Gauge('memory_total', 'Total memory')
memory_used = Gauge('memory_used', 'Used memory')
disk_total = Gauge('disk_total', 'Total disk space')
disk_used = Gauge('disk_used', 'Used disk space')

def collect_metrics():
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpu_usage.labels(core=i).set(percentage)

    mem = psutil.virtual_memory()
    memory_total.set(mem.total)
    memory_used.set(mem.used)

    disk = psutil.disk_usage('/')
    disk_total.set(disk.total)
    disk_used.set(disk.used)

if __name__ == "__main__":
    load_dotenv()
    
    host = os.getenv('EXPORTER_HOST', '0.0.0.0')
    port = int(os.getenv('EXPORTER_PORT', '8000'))

    start_http_server(port, addr=host)
    print(f"Exporter running on {host}:{port}")

    while True:
        collect_metrics()
        time.sleep(15)
