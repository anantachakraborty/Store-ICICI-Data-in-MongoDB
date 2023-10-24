import yfinance as yf
from datetime import datetime, timedelta
from pymongo import MongoClient
from apscheduler.schedulers.background import BackgroundScheduler

# Define MongoDB connection
def initialize_mongodb():
    # Replace with your MongoDB connection details
    mongo_host = "mongodb://localhost:27017/"
    client = MongoClient(mongo_host)
    db = client["stock_data"]
    collection = db["icici_bank"]
    return collection

print("Hello from main.py")

# Define the function to fetch and store data
def fetch_and_store_data(collection):
    # Specify the ICICI Bank ticker
    ticker = "ICICIBANK.NS"

    # Get the current time
    current_time = datetime.now()

    # Calculate the end time (2:15 PM)
    end_time = current_time.replace(hour=14, minute=15, second=0)

    # Check if the current time is within the desired time window (11:15 AM to 2:15 PM)
    if current_time >= end_time:
        # If the current time is beyond 2:15 PM, stop data collection for the day
        print("Data collection stopped for the day.")
        return

    # Calculate the start time (11:15 AM)
    start_time = current_time.replace(hour=11, minute=15, second=0)

    # Fetch 15-minute candle data
    icici_data = yf.download(ticker, start=start_time, end=current_time, interval="15m")

    # Store the data in MongoDB
    if not icici_data.empty:
        data_dict = icici_data.to_dict(orient='records')
        collection.insert_many(data_dict)
        print("Data stored in MongoDB.")

if __name__ == "__main__":
    # Initialize MongoDB connection
    collection = initialize_mongodb()

    # Create a scheduler instance
    scheduler = BackgroundScheduler()

    # Define the schedule to run every 15 minutes
    scheduler.add_job(fetch_and_store_data, 'interval', minutes=15, args=[collection])

    # Start the scheduler
    scheduler.start()

    while True:
        pass
