from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import json 
import requests
import os 
import time

# Kafka Producer with retry
while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers=os.getenv('BOOTSTRAP_SERVERS'),
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("Connected to Kafka broker.")
        break
    except NoBrokersAvailable:
        print("Kafka not available, retrying in 5 seconds...")
        time.sleep(5)

def get_price():
    try:
        URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = {'symbol': 'BTC', 'convert': 'USD'}
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'YOUR_CMC_API_KEY'
        }
        response = requests.get(URL, headers=headers, params=parameters)
        data = response.json()
        price = data['data']['BTC']['quote']['USD']['price']
        return price
    except Exception as e:
        print(f'API error: {e}')
        return None

while True:
    try:
        price = get_price()
        if price:
            producer.send('btc-price', value=price)
            print(f'Current price of Bitcoin: ${price:,.2f}')
        time.sleep(5)
    except KeyboardInterrupt:
        print('\nProducer stopped.')
        break
    except Exception as e:
        print(f"Unexpected error: {e}")

producer.close()
