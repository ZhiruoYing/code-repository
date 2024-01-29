def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Can't divide by zero"
    else:
        return num1 / num2
    
def calculator():
    print("Simple Calculate")
    print("==============================")
    print("Select an operation(1/2/3/4):")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Your choice:")

    num1 = float(input("Enter number: "))
    num2 = float(input("Enter number: "))

    if choice == "1":
        return(add(num1, num2))

    elif choice == "2":
        return(subtract(num1, num2))
    
    elif choice == "3":
        return(multiply(num1, num2))
    
    elif choice == "4":
        return(divide(num1, num2))

    else:
        return("please input the right choice")
    
calculator()


