
print("Welcome to counter")

def increment(counter):
    counter = counter + 1
    return counter

def decrement(counter):
    counter = counter - 1
    return counter

def reset(counter):
    counter = 0
    return counter

counter = 0

while True:
    print("Enter value from (+,-,reset)")
    button = input("Enter value: ")

    if button == "+":
        counter = increment(counter)
    elif button == "-":
        counter = decrement(counter)
    elif button == "reset":
        counter = reset(counter)
    else:
        print("invalid value")

    print("counter =", counter)           
    
       
