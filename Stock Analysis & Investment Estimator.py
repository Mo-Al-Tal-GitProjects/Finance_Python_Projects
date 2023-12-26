
def calculate_stock_price(dividends, growth_rate, required_rate):
    stock_price = dividends / (required_rate - growth_rate)
    return stock_price

def calculate_dividends(stock_price, growth_rate, required_rate):
    dividends = stock_price * (required_rate - growth_rate)
    return dividends

def calculate_growth_rate(stock_price, dividends, required_rate):
    growth_rate = required_rate - (dividends / stock_price)
    return growth_rate

def calculate_required_rate(stock_price, dividends, growth_rate):
    required_rate = (dividends / stock_price) + growth_rate
    return required_rate

def calculate_dividend_yield(stock_price, dividends):
    dividend_yield = (dividends / stock_price) * 100
    return dividend_yield

def calculate_growth_rate_from_historical_data():
    # Add code to input and calculate growth rate from historical data here
    historical_dividends = float(input("Enter historical annual dividends: "))
    current_dividends = float(input("Enter current annual dividends: "))
    years = int(input("Enter the number of years for historical data: "))

    # Calculate growth rate using the formula: (Dividends in current year / Dividends in previous year) ^ (1 / years) - 1
    growth_rate = ((current_dividends / historical_dividends) ** (1 / years)) - 1

    return growth_rate

def calculate_dividends_from_historical_data():
    # Add code to input and calculate dividends from historical data here
    historical_dividends = float(input("Enter historical annual dividends: "))
    years = int(input("Enter the number of years for historical data: "))
    growth_rate = float(input("Enter the estimated growth rate (%): ")) / 100

    # Calculate dividends using the formula: Dividends in current year = Historical dividends * (1 + growth_rate) ^ years
    dividends = historical_dividends * ((1 + growth_rate) ** years)

    return dividends

def calculate_required_rate_from_historical_data():
    # Add code to input and calculate required rate from historical data here
    historical_dividends = float(input("Enter historical annual dividends: "))
    current_stock_price = float(input("Enter current stock price: "))
    years = int(input("Enter the number of years for historical data: "))

    # Calculate required rate of return using the formula: Required Rate = (Dividends in current year / Stock price) ^ (1 / years) - 1
    required_rate = ((historical_dividends / current_stock_price) ** (1 / years)) - 1

    return required_rate
    
def main():

    historical_dividends = None
    growth_rate = None

    while True:
        print("\nStock Price Estimator")
        print("1. Calculate Stock Price")
        print("2. Calculate Dividends")
        print("3. Calculate Growth Rate")
        print("4. Calculate Required Rate")
        print("5. Calculate Dividend Yield")
        print("6. Calculate Growth Rate from Historical Data")
        print("7. Calculate Dividends from Historical Data")
        print("8. Calculate Required Rate from Historical Data")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            dividends = float(input("Enter annual dividends: "))
            growth_rate = float(input("Enter expected growth rate (%): ")) / 100
            required_rate = float(input("Enter required rate of return (%): ")) / 100
            stock_price = calculate_stock_price(dividends, growth_rate, required_rate)
            print(f"Estimated Stock Price: ${stock_price:.2f}")
        elif choice == "2":
            stock_price = float(input("Enter current stock price: "))
            growth_rate = float(input("Enter expected growth rate (%): ")) / 100
            required_rate = float(input("Enter required rate of return (%): ")) / 100
            dividends = calculate_dividends(stock_price, growth_rate, required_rate)
            print(f"Estimated Dividends: ${dividends:.2f}")
        elif choice == "3":
            stock_price = float(input("Enter current stock price: "))
            dividends = float(input("Enter annual dividends: "))
            required_rate = float(input("Enter required rate of return (%): ")) / 100
            growth_rate = calculate_growth_rate(stock_price, dividends, required_rate)
            print(f"Estimated Growth Rate: {growth_rate * 100:.2f}%")
        elif choice == "4":
            stock_price = float(input("Enter current stock price: "))
            dividends = float(input("Enter annual dividends: "))
            growth_rate = float(input("Enter expected growth rate (%): ")) / 100
            required_rate = calculate_required_rate(stock_price, dividends, growth_rate)
            print(f"Required Rate of Return: {required_rate * 100:.2f}%")
        elif choice == "5":
            stock_price = float(input("Enter current stock price: "))
            dividends = float(input("Enter annual dividends: "))
            dividend_yield = calculate_dividend_yield(stock_price, dividends)
            print(f"Dividend Yield: {dividend_yield:.2f}%")
        elif choice == "6":
            growth_rate = calculate_growth_rate_from_historical_data()
            print(f"Estimated Growth Rate from Historical Data: {growth_rate * 100:.2f}%")
        elif choice == "7":
            dividends = calculate_dividends_from_historical_data()
            print(f"Estimated Dividends from Historical Data: ${dividends:.2f}")
        elif choice == "8":
            required_rate = calculate_required_rate_from_historical_data()
            print(f"Required Rate of Return from Historical Data: {required_rate * 100:.2f}%")
        elif choice == "9":
            print("Exiting Stock Price Estimator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
