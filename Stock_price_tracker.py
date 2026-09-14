import requests
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept": "application/json,text/plain,*/*",
}

def fetch_json(url):
    response = requests.get(url, headers=HEADERS, timeout=10)
    if response.status_code == 200:
        return response.json()
    print(f"Failed to fetch page: {response.status_code}")
    return None

def get_stock_price(ticker):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=1d"
    data = fetch_json(url)
    if not data:
        return None

    try:
        meta = data["chart"]["result"][0]["meta"]
        price = meta.get("regularMarketPrice")
        if price is not None:
            return price
        print("Stock price not found.")
        return None
    except (KeyError, IndexError, TypeError):
        print("Stock price not found: unexpected API response.")
        return None

def track_stock_price(ticker, interval=60):
    while True:
        price = get_stock_price(ticker)
        if price:
            print(f"{ticker}: ${price:.2f}")
        time.sleep(interval)

def main():
    print("Welcome to the Stock Price Tracker!")
    ticker = input("Enter the stock ticker symbol (e.g., AAPL, TSLA): ").upper()
    interval = int(input("Enter the update interval (in seconds): "))
    print(f"Tracking stock prices for {ticker} every {interval} seconds...")
    track_stock_price(ticker, interval)

if __name__ == "__main__":
    main()









