Используемые запросы
``` PromQL
cpu_usage{job="exporter"}
(memory_used{job="exporter"} / memory_total{job="exporter"}) * 100
memory_total{job="exporter"} / 1024 / 1024 / 1024
memory_used{job="exporter"} / 1024 / 1024 / 1024
(disk_used{job="exporter"} / disk_total{job="exporter"}) * 100
```