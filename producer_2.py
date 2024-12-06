from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

pay_methods = ['KakaoPay', 'SamsungPay', 'ApplePay']
items = {'A': 1200, 'B': 2800, 'C': 3600} 
customers = ['지드래곤', '탑', '대성', '태양']

try:
    while True:
        order_items = []
        num_items = random.randint(1, 3) 

        available_items = list(items.keys()) 
        for _ in range(num_items):
            item_id = random.choice(available_items) 
            quantity = random.randint(1, 5)
            price = items[item_id]
            order_items.append({"item_id": item_id, "quantity": quantity, "price": price})
            
   
            available_items.remove(item_id)

        order = {
            "order_id": f"{random.randint(1000, 9999)}",
            "customer": random.choice(customers),
            "items": order_items,
            "payment_method": random.choice(pay_methods)
        }

        producer.send('orders', value=order)
        print(f"Produced: {json.dumps(order, indent=4)}")  

        time.sleep(1)
        
except KeyboardInterrupt:
    print("Producer stopped manually.")

finally:
    producer.close()
