import requests

s = {}

def fetch(symbol):

    api_key = 'your_api_key'  
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:

        data = response.json()
        if 'Global Quote' in data and '01. symbol' in data['Global Quote']:
            
            quote = data['Global Quote']
            return {
                'symbol': quote['01. symbol'],
                'price': float(quote['05. price']),
                'change': float(quote['09. change']),
                'change_percent': float(quote['10. change percent'].strip('%'))
            }
        else:

            print(f"Error fetching data for {symbol}: {data.get('Note', 'Unknown error')}")
            return None
        
    else:
        print(f"HTTP Error: {response.status_code}")
        return None

def add_stock(symbol, quantity):

    data = fetch(symbol)
    if data:

        if symbol in s:

            s[symbol]['quantity'] += quantity

        else:

            s[symbol] = {
                'quantity': quantity,
                'data': data
            }

        print(f"Added {quantity} shares of {symbol} to your portfolio.")
    else:
        print(f"Failed to add {symbol} to your portfolio.")

def remove_stock(symbol, quantity):

    if symbol in s:

        if s[symbol]['quantity'] <= quantity:
            del s[symbol]
            print(f"Removed all shares of {symbol} from your portfolio.")

        else:
            s[symbol]['quantity'] -= quantity
            print(f"Removed {quantity} shares of {symbol} from your portfolio.")
    else:
        print(f"{symbol} is not in your portfolio.")

def calculate_portfolio_value():

    total_value = 0.0
    for symbol, stock in s.items():
        total_value += stock['quantity'] * stock['data']['price']
    return total_value

def main():
    
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. View portfolio")
        print("4. View portfolio value")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            add_stock(symbol, quantity)

        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            remove_stock(symbol, quantity)

        elif choice == '3':
            print("Current Portfolio:")
            for symbol, stock in s.items():
                print(f"{symbol}: {stock['quantity']} shares at ${stock['data']['price']:.2f} each")

        elif choice == '4':
            portfolio_value = calculate_portfolio_value()
            print(f"\nPortfolio Value: ${portfolio_value:.2f}")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":

    main()