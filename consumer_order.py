from kafka import KafkaConsumer
import json
from tabulate import tabulate

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    group_id='customer_info_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    order = message.value
    print(f"\n주문 ID: {order['order_id']} (이름: {order['customer']})")
    

    table = [[item['item_id'], item['quantity'], item['price']] for item in order['items']]
    print(tabulate(table, headers=["Item ID", "수량", "가격"], tablefmt="grid"))

