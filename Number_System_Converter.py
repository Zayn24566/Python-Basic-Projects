# ============================================
#       NUMBER SYSTEM CONVERTER
#   Binary | Octal | Decimal | Hexadecimal
# ============================================

# ── Conversion Functions ──────────────────────────────────────────────────────

def decimal_to_binary(n):
    return bin(n)[2:]          # bin() gives '0b101' → slice off '0b'

def decimal_to_octal(n):
    return oct(n)[2:]          # oct() gives '0o17'  → slice off '0o'

def decimal_to_hex(n):
    return hex(n)[2:].upper()  # hex() gives '0xff'  → slice off '0x', uppercase

def binary_to_decimal(b):
    return int(b, 2)           # int(value, base)

def octal_to_decimal(o):
    return int(o, 8)

def hex_to_decimal(h):
    return int(h, 16)


# ── Validate input for a given base ──────────────────────────────────────────
def is_valid(value, base):
    valid_chars = {
        2:  "01",
        8:  "01234567",
        10: "0123456789",
        16: "0123456789ABCDEFabcdef",
    }
    return all(ch in valid_chars[base] for ch in value)


# ── Get valid number input from user ─────────────────────────────────────────
def get_number(prompt, base):
    while True:
        value = input(prompt).strip()
        if not value:
            print("  ⚠  Input cannot be empty.\n")
        elif not is_valid(value, base):
            base_names = {2: "Binary", 8: "Octal", 10: "Decimal", 16: "Hexadecimal"}
            print(f"  ⚠  Invalid {base_names[base]} number. Please try again.\n")
        else:
            return value


# ── Display full conversion table ─────────────────────────────────────────────
def show_results(decimal_value):
    binary  = decimal_to_binary(decimal_value)
    octal   = decimal_to_octal(decimal_value)
    hexa    = decimal_to_hex(decimal_value)

    print("\n" + "=" * 45)
    print("         🔢  CONVERSION RESULTS")
    print("=" * 45)
    print(f"  Decimal     (Base 10) :  {decimal_value}")
    print(f"  Binary      (Base  2) :  {binary}")
    print(f"  Octal       (Base  8) :  {octal}")
    print(f"  Hexadecimal (Base 16) :  {hexa}")
    print("=" * 45)


# ── Show conversion menu ──────────────────────────────────────────────────────
def show_menu():
    print("\n  Select input type:")
    print("  [1] Decimal     → Binary, Octal, Hex")
    print("  [2] Binary      → Decimal, Octal, Hex")
    print("  [3] Octal       → Decimal, Binary, Hex")
    print("  [4] Hexadecimal → Decimal, Binary, Octal")
    print("  [0] Exit")

    while True:
        choice = input("\n  Enter choice (0-4): ").strip()
        if choice in ("0", "1", "2", "3", "4"):
            return choice
        print("  ⚠  Invalid choice. Please enter 0, 1, 2, 3, or 4.")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("=" * 45)
    print("      🔢  NUMBER SYSTEM CONVERTER")
    print("  Binary | Octal | Decimal | Hexadecimal")
    print("=" * 45)

    while True:
        choice = show_menu()

        if choice == "0":
            print("\n  Goodbye! 👋\n")
            break

        elif choice == "1":
            val = get_number("\n  Enter Decimal number: ", 10)
            show_results(int(val))

        elif choice == "2":
            val = get_number("\n  Enter Binary number (e.g. 1010): ", 2)
            show_results(binary_to_decimal(val))

        elif choice == "3":
            val = get_number("\n  Enter Octal number (e.g. 17): ", 8)
            show_results(octal_to_decimal(val))

        elif choice == "4":
            val = get_number("\n  Enter Hexadecimal number (e.g. 1F): ", 16)
            show_results(hex_to_decimal(val))

        again = input("\n  🔁  Convert another? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  Goodbye! 👋\n")
            break


if __name__ == "__main__":
    main()