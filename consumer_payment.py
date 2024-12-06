from kafka import KafkaConsumer
import json
from tabulate import tabulate  

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    group_id='payment_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    order = message.value

    total_price = sum(item['price'] * item['quantity'] for item in order['items'])
   
    print(f"\n주문 ID {order['order_id']} : {total_price} 원")
    print(f"결제 방식: {order['payment_method']}\n")
