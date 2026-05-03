# ============================================
#      MULTIPLICATION TABLE GENERATOR
# ============================================

# ── Get a valid positive integer from user ────────────────────────────────────
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("  ⚠  Please enter a number greater than 0.\n")
            else:
                return value
        except ValueError:
            print("  ⚠  Invalid input. Please enter a whole number.\n")


# ── Generate and display single table ────────────────────────────────────────
def single_table(number, start, end):
    print("\n" + "=" * 35)
    print(f"   📋  Multiplication Table of {number}")
    print("=" * 35)
    for i in range(start, end + 1):
        result = number * i
        print(f"   {number:>3}  x  {i:<3}  =  {result}")
    print("=" * 35)


# ── Generate and display range of tables ─────────────────────────────────────
def range_tables(start_num, end_num, start, end):
    print("\n" + "=" * 55)
    print(f"   📋  Multiplication Tables from {start_num} to {end_num}")
    print("=" * 55)

    # Print column headers
    header = "  Mult  |"
    for n in range(start_num, end_num + 1):
        header += f"  {n:>4}  |"
    print(header)
    print("-" * len(header))

    # Print each row
    for i in range(start, end + 1):
        row = f"   x{i:<3}  |"
        for n in range(start_num, end_num + 1):
            row += f"  {n * i:>4}  |"
        print(row)

    print("=" * len(header))


# ── Show main menu ────────────────────────────────────────────────────────────
def show_menu():
    print("\n  What do you want to generate?")
    print("  [1] Single number table")
    print("  [2] Range of tables (e.g. 2 to 10)")
    print("  [0] Exit")

    while True:
        choice = input("\n  Enter choice (0/1/2): ").strip()
        if choice in ("0", "1", "2"):
            return choice
        print("  ⚠  Invalid choice. Enter 0, 1, or 2.")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("=" * 45)
    print("    📊  MULTIPLICATION TABLE GENERATOR")
    print("=" * 45)

    while True:
        choice = show_menu()

        if choice == "0":
            print("\n  Goodbye! 👋\n")
            break

        elif choice == "1":
            number = get_positive_int("\n  Enter the number: ")
            print("\n  Default range is 1 to 10.")
            custom = input("  Use custom range? (yes/no): ").strip().lower()
            if custom in ("yes", "y"):
                start = get_positive_int("  Start from: ")
                end   = get_positive_int("  End at    : ")
                if start > end:
                    print("  ⚠  Start must be less than or equal to End. Using default 1-10.")
                    start, end = 1, 10
            else:
                start, end = 1, 10

            single_table(number, start, end)

        elif choice == "2":
            print("\n  Enter the range of tables to generate.")
            start_num = get_positive_int("  From table: ")
            end_num   = get_positive_int("  To table  : ")
            if start_num > end_num:
                print("  ⚠  Start must be <= End. Swapping values.")
                start_num, end_num = end_num, start_num

            print("\n  Default row range is 1 to 10.")
            custom = input("  Use custom row range? (yes/no): ").strip().lower()
            if custom in ("yes", "y"):
                start = get_positive_int("  Start from: ")
                end   = get_positive_int("  End at    : ")
                if start > end:
                    print("  ⚠  Start must be <= End. Using default 1-10.")
                    start, end = 1, 10
            else:
                start, end = 1, 10

            range_tables(start_num, end_num, start, end)

        print()
        again = input("  🔁  Generate another? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  Goodbye! 👋\n")
            break


if __name__ == "__main__":
    main()