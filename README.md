# Stock Data Collector

## Overview

This Python program is designed to collect and store real-time 15-minute candle data for ICICI Bank (ICICIBANK.NS) from Yahoo Finance. The data is collected daily from 11:15 AM to 2:15 PM for a week. Due to the 15-minute delay in the Yahoo Finance library, the program starts logging at 11:15 AM to capture data for the 11:00 AM time interval.

## Prerequisites

Before running this program, you need to have the following installed on your system:

- Python
- pip (Python package manager)
- MongoDB (make sure the MongoDB server is running)

You can install the required Python libraries using pip:

```bash
pip install yfinance pymongo apscheduler
