from kafka import KafkaProducer
import json
import time
import random

# Kafka Producer 설정
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # JSON 직렬화
)

# 데이터 샘플
pay_methods = ['KakaoPay', 'SamsungPay', 'ApplePay']
items = {'A': 1200, 'B': 2800, 'C': 3600}  # 각 아이템의 가격
customers = ['Karina', 'Winter', 'Ningning', 'Giselle']

# 1초마다 메시지 생성
try:
    while True:
        order_items = []
        num_items = random.randint(1, 3)  # 주문 항목 개수 랜덤 선택

        # 주문 항목 생성 (중복되지 않게 아이템 추가)
        available_items = list(items.keys())  # 아이템 리스트 복사
        for _ in range(num_items):
            item_id = random.choice(available_items)  # 아이템을 랜덤으로 선택
            quantity = random.randint(1, 5)
            price = items[item_id]
            order_items.append({"item_id": item_id, "quantity": quantity, "price": price})
            
            # 중복을 방지하기 위해 해당 아이템을 사용한 후 리스트에서 제거
            available_items.remove(item_id)

        order = {
            "order_id": f"{random.randint(1000, 9999)}",
            "customer": random.choice(customers),
            "items": order_items,
            "payment_method": random.choice(pay_methods)
        }
        
        # 메시지 전송
        producer.send('orders', value=order)
        print(f"Produced: {json.dumps(order, indent=4)}")  # 보기 쉽게 출력
        
        # 1초 대기
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Producer stopped manually.")

finally:
    producer.close()
