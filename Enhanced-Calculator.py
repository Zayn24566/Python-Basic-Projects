print("Welcome To My Calculator")
numbers = []
opr = []
a = int(input("Enter first number: "))
numbers.append(a)
while True:
    operator = input("Enter operator (+, -, *, /) or press [=] to calculate: ")
    if operator == "=":
        break
    opr.append(operator)
    b = int(input("Enter next number: "))
    numbers.append(b)

total = [numbers[0]]

def sum(total, b):
    total[0] = total[0] + b

def sub(total, b):
    total[0] = total[0] - b

def mul(total, b):
    total[0] = total[0] * b

def div(total, b):
    total[0] = total[0] / b
i = 0
for op in opr:

    if op == "+":
        sum(total, numbers[i+1])
    elif op == "-":
        sub(total, numbers[i+1])
    elif op == "*":
        mul(total, numbers[i+1])
    elif op == "/":
        div(total, numbers[i+1])

    i=i+1
print("Answer of calculation =", total)
      
