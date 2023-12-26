
def calculate_ocf(ebit, depreciation, taxes):
    return ebit + depreciation - taxes

def calculate_ncs(ending_net_fixed_assets, beginning_net_fixed_assets, depreciation):
    return ending_net_fixed_assets - beginning_net_fixed_assets + depreciation

def calculate_delta_nwc(ending_nwc, beginning_nwc):
    return ending_nwc - beginning_nwc

def calculate_cash_flow_from_assets(ocf, ncs, delta_nwc):
    return ocf - ncs - delta_nwc

def calculate_cfe(ocf, ncs, net_borrowing):
    return ocf - ncs + net_borrowing

def calculate_fcf(ocf, ncs):
    return ocf - ncs

def calculate_dcf(cash_flows, discount_rate):
    dcf_value = 0
    for i, cash_flow in enumerate(cash_flows, start=1):
        dcf_value += cash_flow / (1 + discount_rate) ** i
    return dcf_value

def main():
    while True:
        print("\nCash Flow and OCF Calculator")
        print("----------------------------")
        print("1. Calculate Operating Cash Flow (OCF)")
        print("2. Calculate Net Capital Spending (NCS)")
        print("3. Calculate Change in Net Working Capital (ΔNWC)")
        print("4. Calculate Cash Flow from Assets")
        print("5. Calculate Cash Flow to Equity (CFE)")
        print("6. Calculate Free Cash Flow (FCF)")
        print("7. Calculate Discounted Cash Flow (DCF) Valuation")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            ebit = float(input("Enter EBIT: "))
            depreciation = float(input("Enter Depreciation: "))
            taxes = float(input("Enter Taxes: "))
            ocf = calculate_ocf(ebit, depreciation, taxes)
            print(f"Operating Cash Flow (OCF): {ocf}")

        elif choice == "2":
            ending_net_fixed_assets = float(input("Enter Ending Net Fixed Assets: "))
            beginning_net_fixed_assets = float(input("Enter Beginning Net Fixed Assets: "))
            depreciation = float(input("Enter Depreciation: "))
            ncs = calculate_ncs(ending_net_fixed_assets, beginning_net_fixed_assets, depreciation)
            print(f"Net Capital Spending (NCS): {ncs}")

        elif choice == "3":
            ending_nwc = float(input("Enter Ending NWC: "))
            beginning_nwc = float(input("Enter Beginning NWC: "))
            delta_nwc = calculate_delta_nwc(ending_nwc, beginning_nwc)
            print(f"Change in Net Working Capital (ΔNWC): {delta_nwc}")

        elif choice == "4":
            ocf = float(input("Enter Operating Cash Flow (OCF): "))
            ncs = float(input("Enter Net Capital Spending (NCS): "))
            delta_nwc = float(input("Enter Change in Net Working Capital (ΔNWC): "))
            cash_flow_from_assets = calculate_cash_flow_from_assets(ocf, ncs, delta_nwc)
            print(f"Cash Flow from Assets: {cash_flow_from_assets}")

        elif choice == "5":
            ocf = float(input("Enter Operating Cash Flow (OCF): "))
            ncs = float(input("Enter Net Capital Spending (NCS): "))
            net_borrowing = float(input("Enter Net Borrowing: "))
            cfe = calculate_cfe(ocf, ncs, net_borrowing)
            print(f"Cash Flow to Equity (CFE): {cfe}")

        elif choice == "6":
            ocf = float(input("Enter Operating Cash Flow (OCF): "))
            ncs = float(input("Enter Net Capital Spending (NCS): "))
            fcf = calculate_fcf(ocf, ncs)
            print(f"Free Cash Flow (FCF): {fcf}")

        elif choice == "7":
            cash_flows = []
            num_years = int(input("Enter the number of years for future cash flows: "))
            for i in range(num_years):
                cash_flow = float(input(f"Enter Cash Flow for Year {i+1}: "))
                cash_flows.append(cash_flow)
            discount_rate = float(input("Enter Discount Rate (as a decimal): "))
            dcf_value = calculate_dcf(cash_flows, discount_rate)
            print(f"Discounted Cash Flow (DCF) Valuation: {dcf_value}")

        elif choice == "8":
            print("Exiting. Thank you for using the Cash Flow and OCF Calculator!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
