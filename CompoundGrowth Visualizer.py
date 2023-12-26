import math
import matplotlib.pyplot as plt

def calculate_compounding_periods(I_Y, PV, FV, PMT, compounding_frequency):
    try:
        if I_Y <= 0 or compounding_frequency <= 0:
            raise ValueError("Interest rate and compounding frequency must be greater than zero.")

        effective_rate = (1 + I_Y) ** (1 / compounding_frequency) - 1
        if PMT == 0:
            # Formula for compound interest without periodic payments
            N = math.log(FV / PV) / math.log(1 + effective_rate)
        else:
            # Formula for compound interest with periodic payments
            N = math.log((FV * effective_rate + PMT) / (PV * effective_rate + PMT)) / math.log(1 + effective_rate)

        return N * compounding_frequency  # Adjust for the number of periods per year

    except (ZeroDivisionError, ValueError) as e:
        print(f"Error: {e}")

def plot_investment_growth(PV, I_Y, PMT, N, compounding_frequency):
    principal_balances = []
    interest_balances = []
    total_balances = []
    periods = range(int(N * compounding_frequency))
    effective_rate = (1 + I_Y) ** (1 / compounding_frequency) - 1

    for period in periods:
        interest = PV * ((1 + effective_rate) ** period) - PV if PMT == 0 else PMT * (((1 + effective_rate) ** period - 1) / effective_rate)
        principal = PV if PMT == 0 else PMT * period
        total_balance = principal + interest

        principal_balances.append(principal)
        interest_balances.append(interest)
        total_balances.append(total_balance)

    plt.figure(figsize=(12, 8))
    plt.plot(periods, principal_balances, label='Principal', color='green', linestyle='--')
    plt.plot(periods, interest_balances, label='Interest', color='red', linestyle=':')
    plt.plot(periods, total_balances, label='Total Balance', color='blue')
    
    plt.xlabel('Number of Periods')
    plt.ylabel('Balance')
    plt.title(f'Investment Growth Over Time (Rate: {I_Y*100}%, Periods: {N}, Frequency: {compounding_frequency}/yr)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("Compounding Periods Calculator")
    print("------------------------------")

    while True:
        try:
            I_Y = float(input("Enter the annual interest rate (I/Y as a decimal): "))
            PV = float(input("Enter the present value (PV): "))
            FV = float(input("Enter the future value (FV): "))
            PMT = float(input("Enter additional periodic payment (PMT, optional, enter 0 if none): "))
            compounding_frequency = int(input("Enter the number of compounding periods per year (e.g., 1 for annual, 12 for monthly): "))

            if any(value < 0 for value in [I_Y, PV, FV, PMT]):
                raise ValueError("Negative values are not valid.")

            N = calculate_compounding_periods(I_Y, PV, FV, PMT, compounding_frequency)
            if N is not None:
                print(f"The number of compounding periods (N) is: {N:.2f}")

        except ValueError as e:
            print(f"Invalid input: {e}")

        plot_choice = input("Do you want to see a plot of investment growth over time? (yes/no): ")
        if plot_choice.lower() == 'yes':
            plot_investment_growth(PV, I_Y, PMT, N, compounding_frequency)

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
