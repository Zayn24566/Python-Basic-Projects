print("Welcome to ATM-Banking")

print ("Insert your card----")

correct_pin = 2006
a = int(input("Enter your 4-digit code== "))

if a == correct_pin:
    print("Successfully Login !!!")

    current_balance = 50000

    def check_balance(balance):
        print("Your Current Balance is == ", balance)
        return balance


    def deposit(balance):
        amount = int(input("Enter Amount== "))
        balance = balance + amount
        print("Successfully Deposited==", amount)
        return balance

    def withdraw(balance):
        amount = int(input("Enter amount you want to withdraw== "))
        balance = balance - amount
        print("You have successfully withdrawn amount==", amount)
        return balance

    def change_pin(pin):
        new_pin = int(input("Enter new pin== "))
        print("Your new pin is", new_pin)
        return new_pin

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        button = input("Choose option: ")

        if button == "1":
            current_balance = check_balance(current_balance)

        elif button == "2":
            current_balance = deposit(current_balance)

        elif button == "3":
            current_balance = withdraw(current_balance)

        elif button == "4":
            correct_pin = change_pin(correct_pin)

        elif button == "5":
            print("Thank you for using ATM Banking")
            break

        else:
            print("Invalid choice")
            

else:
    print("Invalid code")

   

 

