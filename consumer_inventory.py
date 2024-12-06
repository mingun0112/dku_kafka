from kafka import KafkaConsumer
import json
from tabulate import tabulate

inventory = {"A": 1000, "B": 3000, "C": 2200}

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    group_id='inventory_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def display_inventory():
    table = [[item, stock] for item, stock in inventory.items()]
    print("\n현재 재고:")
    print(tabulate(table, headers=["Item ID", "재고"], tablefmt="grid"))


for message in consumer:
    order = message.value
    print(f"\n주문 내역: {order['order_id']}")
    for item in order['items']:
        item_id = item['item_id']
        quantity = item['quantity']
        if inventory.get(item_id, 0) >= quantity:
            inventory[item_id] -= quantity
            print(f"Item {item_id}:, 잔여량: {inventory[item_id]}")
        else:
            print(f"Item {item_id}: 재고 불충분 {order['order_id']}")

    display_inventory()
