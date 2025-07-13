def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Divide 0 is not allowed\n")
    else:
        return a / b

while True:
    print("Menu")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. Exit")
    
    choice = int(input("Enter ur choice: "))
    
    if choice == 5:
        print("Exiting program")
        break
    
    num1 = int(input("Enter ur first number  : "))
    num2 = int(input("Enter ur second number : "))
    
    if choice == 1:
        print("Sum: ", add(num1, num2))
    elif choice == 2:
        print("Sub: ", subtract(num1, num2))
    elif choice == 3:
        print("Mul: ", multiply(num1, num2))
    elif choice == 4:
        print("Div: ", divide(num1, num2))
    else:
        print("Invalid choice, type again!!")
    