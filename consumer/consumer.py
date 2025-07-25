from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
import json
import csv
import os
import time
from datetime import datetime

# Retry until Kafka is ready
while True:
    try:
        consumer = KafkaConsumer(
            'btc-price',
            bootstrap_servers=os.getenv('BOOTSTRAP_SERVERS'),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        print("Connected to Kafka broker.")
        break
    except NoBrokersAvailable:
        print("Kafka not available, retrying in 5 seconds...")
        time.sleep(5)

# CSV setup
csv_dir = 'output'
csv_file = os.path.join(csv_dir, 'btc_prices.csv')
os.makedirs(csv_dir, exist_ok=True)

if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'BTC Price (USD)'])

ALERT_THRESHOLD = 120000

print("Consumer started. Listening for Bitcoin price data...")

try:
    for message in consumer:
        price = message.value
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, price])

        print(f"Saved to CSV: {timestamp} | BTC Price: ${price:,.2f}")
        
        if price > ALERT_THRESHOLD:
            print(f"\n🚨 ALERT: BTC price is above ${ALERT_THRESHOLD:,}! Current Price: ${price:,.2f}\n")

except KeyboardInterrupt:
    print("\nConsumer stopped.")
