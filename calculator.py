#Python Program to make simple calculator with functions

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")

while True:
    option = input("Enter a Option: ")

    if option in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if option == '1':
            print("Addition of ", num1, " and ", num2, " is ", add(num1, num2))
        elif option == '2':
            print("Subtraction of ", num1, " and ", num2, " is ", sub(num1, num2))
        elif option == '3':
            print("Multiplication of ", num1, " and ", num2, " is ", multiply(num1, num2))
        elif option == '4':
            print("Division of ", num1, " and ", num2, " is ", divide(num1, num2))
    elif option == '5':
        break
    else:
        print("Invalid Entry!")
