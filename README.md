# MindYourBusinessClass Telegram Bot for chep business class tickets search

A Telegram bot that helps users find the cheapest business class flights using the Amadeus API. 
Built with Python, this bot allows users to enter a route and date, and it returns real-time flight options directly in Telegram.

---

## Features

- Search for flights by IATA airport codes and date (Full Airport name search - to be added)
- Filters only business class offers
- Returns carrier code, route, departure time, and price (Full carrier name search - to be added)
- Telegram bot interface
- API keys and tokens secured via `.env`

---

## Tech Stack

- Python 3.8+
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [Amadeus Self-Service API](https://developers.amadeus.com/)
- python-dotenv

---

## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/flight-search-telegram-bot.git
cd flight-search-telegram-bot```

### 2. Install Dependencies
```
pip install -r requirements.txt


### 3. Create a .env File
Add your API keys to a .env file in the root:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_API_SECRET=your_amadeus_api_secret```

You can get the Telegram token via @BotFather
Amadeus credentials are available from developers.amadeus.com

## Usage
Run the bot:
```python main.py```

Then, in Telegram:

/find LAX JFK 2025-06-10


Example output:

$1240.00 | BA LAX→LHR ➔ BA LHR→JFK | 2025-06-10 16:35
$1315.00 | LH LAX→FRA ➔ LH FRA→JFK | 2025-06-10 14:20


---
Project Structure
telegram-bot/
├── main.py               # Bot entry point
├── config.py             # Loads API keys from .env
├── flight_search.py      # Handles API logic
├── requirements.txt
├── .env                  # Your secret keys (not committed)
└── README.md
