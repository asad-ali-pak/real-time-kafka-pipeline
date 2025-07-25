# Real-Time Kafka Pipeline – BTC Price Monitor

A real-time data pipeline that fetches live Bitcoin (BTC) prices from the CoinMarketCap API, processes them using Apache Kafka, stores the price history in a CSV file, and triggers alerts via a Kafka Consumer when the price crosses a predefined threshold.

## Features
- **Real-time Kafka Producer & Consumer**: Streams BTC price data using Kafka for real-time processing.
- **CoinMarketCap API Integration**: Fetches live Bitcoin prices from the CoinMarketCap API.
- **CSV Storage**: Stores BTC price history in a CSV file for record-keeping.
- **Threshold-Based Alerts**: Notifies via Kafka Consumer when the BTC price crosses a specified threshold.
- **Fully Containerized**: Uses Docker and Docker Compose for easy setup and deployment.

## Folder Structure
```
real-time-kafka-pipeline/
├── consumer/
│   ├── consumer.py           # Kafka Consumer script for processing and alerting
│   ├── Dockerfile            # Dockerfile for the Consumer
│   └── requirements.txt      # Dependencies for the Consumer
├── producer/
│   ├── producer.py           # Kafka Producer script for fetching and streaming BTC prices
│   ├── Dockerfile            # Dockerfile for the Producer
│   └── requirements.txt      # Dependencies for the Producer
├── output/
│   └── btc_prices.csv        # CSV file storing BTC price history
├── docker-compose.yml        # Docker Compose configuration for orchestrating services
├── README.md
```

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed
- A valid [CoinMarketCap API key](https://coinmarketcap.com/api/)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/asad-ali-pak/real-time-kafka-pipeline.git
   cd real-time-kafka-pipeline
   ```

2. **Add Your CoinMarketCap API Key**
   - Open `producer/producer.py` and update the API key in the headers:
     ```python
     headers = {
         'X-CMC_PRO_API_KEY': 'YOUR_CMC_API_KEY'
     }
     ```

3. **Run the Project**
   ```bash
   docker-compose up --build -d
   ```
   This command will:
   - Start Zookeeper and Kafka brokers
   - Launch the Producer container to fetch and stream BTC prices
   - Launch the Consumer container to process prices and trigger alerts

### Sample Output
The BTC price history is saved in `output/btc_prices.csv` with the following format:
```
timestamp,price_usd
2025-07-19 12:30:00,118146.7556732
```

## Contact
Made with ❤️ by [Asad Ali](https://github.com/asad-ali-pak).  
Feel free to contribute, open an issue, or reach out for questions!