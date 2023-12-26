# Import datetime module for date validation
from datetime import datetime

# Define an empty list to store bond purchase records
bond_investments = []

# Function to add a bond purchase record
def add_bond_investment():
    bond_name = input("Enter the name of the bond: ")
    
    # Validate and parse the purchase date
    while True:
        try:
            purchase_date = input("Enter the purchase date (YYYY-MM-DD): ")
            datetime.strptime(purchase_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    face_value = float(input("Enter the face value of the bond: "))
    purchase_price = float(input("Enter the purchase price: "))
    coupon_rate = float(input("Enter the annual coupon rate (%): "))
    years_to_maturity = int(input("Enter the years to maturity: "))
    
    bond_record = {
        "Bond Name": bond_name,
        "Purchase Date": purchase_date,
        "Face Value": face_value,
        "Purchase Price": purchase_price,
        "Coupon Rate": coupon_rate,
        "Years to Maturity": years_to_maturity
    }
    
    bond_investments.append(bond_record)
    print("Bond investment added successfully.")

# Function to display all bond purchase records
def display_bond_investments():
    print("\nBond Investment Records:")
    for idx, bond in enumerate(bond_investments, start=1):
        print(f"Bond #{idx}")
        for key, value in bond.items():
            print(f"{key}: {value}")
        print()

# Function to calculate the yield to maturity (YTM) for a bond
def calculate_ytm(face_value, purchase_price, coupon_rate, years_to_maturity):
    # Calculate YTM using the formula for a bond's YTM
    coupon = face_value * (coupon_rate / 100)
    ytm = ((face_value + (coupon * years_to_maturity)) / purchase_price) ** (1 / years_to_maturity) - 1
    ytm *= 100  # Convert YTM to percentage
    return ytm

# Function to calculate the total value of bond investments
def calculate_total_investment_value():
    total_value = sum(bond['Purchase Price'] for bond in bond_investments)
    print(f"Total Value of Bond Investments: ${total_value:.2f}")

def filter_bonds(attribute, value, bond_list):
    filtered_bonds = [bond for bond in bond_list if str(bond.get(attribute, '')).lower() == str(value).lower()]
    return filtered_bonds

def sort_bonds(attribute, ascending, bond_list):
    return sorted(bond_list, key=lambda bond: bond.get(attribute, ''), reverse=not ascending)

# New function to handle filtering and sorting
def filter_and_sort_bonds():
    attribute = input("Enter the attribute to filter by (e.g., 'Bond Name', 'Years to Maturity'): ")
    value = input(f"Enter the value for {attribute}: ")
    order = input("Sort in ascending order? (yes/no): ")
    ascending = order.lower() == 'yes'

    filtered_bonds = filter_bonds(attribute, value, bond_investments)
    sorted_bonds = sort_bonds(attribute, ascending, filtered_bonds)

    print("\nFiltered and Sorted Bond Investment Records:")
    for idx, bond in enumerate(sorted_bonds, start=1):
        print(f"Bond #{idx}")
        for key, value in bond.items():
            print(f"{key}: {value}")
        print()

def calculate_compound_interest(face_value, coupon_rate, reinvestment_rate, years_to_maturity, frequency):

    coupon_payment = face_value * (coupon_rate / 100) / frequency
    periods = years_to_maturity * frequency
    future_value = 0

    for period in range(1, periods + 1):
        future_value += coupon_payment * ((1 + reinvestment_rate / 100 / frequency) ** (periods - period + 1))

    return future_value

def project_cash_flows(face_value, coupon_rate, years_to_maturity, frequency):

    coupon_payment = face_value * (coupon_rate / 100) / frequency
    cash_flows = [coupon_payment] * (years_to_maturity * frequency)
    cash_flows[-1] += face_value  # Add the face value to the last payment
    return cash_flows

def handle_compound_interest():
    bond_idx = int(input("Enter the bond number to calculate compound interest for: ")) - 1
    reinvestment_rate = float(input("Enter the annual reinvestment rate (%): "))
    frequency = int(input("Enter the frequency of coupon payments per year: "))

    if 0 <= bond_idx < len(bond_investments):
        bond = bond_investments[bond_idx]
        future_value = calculate_compound_interest(bond["Face Value"], bond["Coupon Rate"], reinvestment_rate, bond["Years to Maturity"], frequency)
        print(f"Future value of {bond['Bond Name']}'s coupon payments: ${future_value:.2f}")
    else:
        print("Invalid bond number.")

def handle_cash_flow_projection():
    bond_idx = int(input("Enter the bond number to project cash flows for: ")) - 1
    frequency = int(input("Enter the frequency of coupon payments per year: "))

    if 0 <= bond_idx < len(bond_investments):
        bond = bond_investments[bond_idx]
        cash_flows = project_cash_flows(bond["Face Value"], bond["Coupon Rate"], bond["Years to Maturity"], frequency)
        print(f"Cash flows for {bond['Bond Name']}:")
        for period, cash_flow in enumerate(cash_flows, start=1):
            print(f"Period {period}: ${cash_flow:.2f}")
    else:
        print("Invalid bond number.")

# Main menu for the bond investment tracker
def main():
    while True:
        print("\nBond Investment Tracker")
        print("1. Add Bond Investment")
        print("2. Display Bond Investments")
        print("3. Calculate YTM for a Bond")
        print("4. Calculate Total Investment Value")
        print("5. Filter and Sort Bonds")
        print("6. Calculate Compound Interest")
        print("7. Project Cash Flows")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_bond_investment()
        elif choice == "2":
            display_bond_investments()
        elif choice == "3":
            # Calculate YTM for a selected bond
            display_bond_investments()
            try:
                bond_idx = int(input("Enter the bond number to calculate YTM: ")) - 1
                if 0 <= bond_idx < len(bond_investments):
                    bond = bond_investments[bond_idx]
                    ytm = calculate_ytm(bond["Face Value"], bond["Purchase Price"], bond["Coupon Rate"], bond["Years to Maturity"])
                    print(f"Yield to Maturity (YTM) for {bond['Bond Name']}: {ytm:.2f}%")
                else:
                    print("Invalid bond number.")
            except ValueError:
                print("Invalid input. Please enter a valid bond number.")
        elif choice == "4":
            calculate_total_investment_value()
        elif choice == "5":
                filter_and_sort_bonds()
        elif choice == "6":
            handle_compound_interest()
        elif choice == "7":
            handle_cash_flow_projection()
        elif choice == "8":
            print("Exiting Bond Investment Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            
if __name__ == "__main__":
    main()
