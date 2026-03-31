def calculate_portfolio():
    # Predefined stock prices (Hardcoded dictionary)
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 150,
        "MSFT": 400,
        "AMZN": 175
    }

    portfolio = {}
    total_value = 0

    print("--- Welcome to your Stock Portfolio Tracker ---")
    print(f"Available Stocks: {', '.join(stock_prices.keys())}\n")

    while True:
        symbol = input("Enter Stock Symbol (or 'done' to finish): ").upper()
        if symbol == 'DONE':
            break
        
        if symbol in stock_prices:
            try:
                shares = int(input(f"How many shares of {symbol} do you own? "))
                portfolio[symbol] = shares
                
                # Calculation: Price * Quantity
                investment = shares * stock_prices[symbol]
                total_value += investment
                print(f"Added {shares} shares of {symbol}. Current Value: ${investment}")
            except ValueError:
                print("Invalid input. Please enter a number for shares.")
        else:
            print("Stock not found in our database. Please try AAPL, TSLA, GOOGL, MSFT, or AMZN.")

    # Display Final Results
    print("\n--- Final Portfolio Summary ---")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares")
    
    print(f"\nTotal Investment Value: ${total_value}")

    # Optional: Save to a .txt file
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("========================\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares\n")
        f.write(f"Total Value: ${total_value}")
    print("\nSummary saved to 'portfolio_summary.txt'")

if __name__ == "__main__":
    calculate_portfolio()
