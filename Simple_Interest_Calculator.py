# ============================================
#        Simple Interest Calculator
# ============================================
# Formula: SI = (Principal * Rate * Time) / 100
# Total Amount = Principal + SI

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("  ⚠  Please enter a value greater than 0.\n")
            else:
                return value
        except ValueError:
            print("  ⚠  Invalid input. Please enter a numeric value.\n")


def calculate_simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    total = principal + si
    return si, total


def display_results(principal, rate, time, si, total):
    print("\n" + "=" * 45)
    print("           📊  CALCULATION RESULTS")
    print("=" * 45)
    print(f"  Principal Amount  : Rs. {principal:,.2f}")
    print(f"  Annual Rate       : {rate}%")
    print(f"  Time Period       : {time} year(s)")
    print("-" * 45)
    print(f"  Simple Interest   : Rs. {si:,.2f}")
    print(f"  Total Amount      : Rs. {total:,.2f}")
    print("=" * 45)


def main():
    print("=" * 45)
    print("      💰  SIMPLE INTEREST CALCULATOR")
    print("=" * 45)
    print("  Formula: SI = (P × R × T) / 100\n")

    while True:
        print("Enter the following details:\n")

        principal = get_positive_float("  Principal Amount (Rs.): ")
        rate      = get_positive_float("  Annual Interest Rate (%): ")
        time      = get_positive_float("  Time Period (years): ")

        si, total = calculate_simple_interest(principal, rate, time)
        display_results(principal, rate, time, si, total)

        print()
        again = input("  🔁  Calculate again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  Thank you for using the Interest Calculator. Goodbye! 👋\n")
            break
        print()


if __name__ == "__main__":
    main()