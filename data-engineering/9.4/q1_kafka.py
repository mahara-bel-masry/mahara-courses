import json
from kafka import KafkaProducer, KafkaConsumer
p = KafkaProducer(bootstrap_servers="localhost:9092",
                  value_serializer=lambda v: json.dumps(v).encode())
for i in range(1, 4):
    p.send("orders", {"id": i, "amount": i * 100})
p.flush()
c = KafkaConsumer("orders", bootstrap_servers="localhost:9092",
                  auto_offset_reset="earliest", group_id="g1",
                  consumer_timeout_ms=5000)
total = 0
for m in c:
    total += json.loads(m.value)["amount"]
print(total)
