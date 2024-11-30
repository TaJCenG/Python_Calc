
#ARITHMETIC CALCULATIONS
def arithmetic_Calculations(a, b, operation):
    if operation == 'addition':
        return a+b
    elif operation == 'subtraction':
        return a-b
    elif operation == 'multiplication':
        return a*b
    elif operation == 'division':
        if b==0:
            return "Errror: Division by Zero"
        return a/b
    else: 
        return "Error: invalid operation"
    
def main():
    try:
        a = float(input ("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input, please enter numeric values.")
        return
    operation = input("Enter the operation(addition, subtraction, multiplication, division").lower()
    result = arithmetic_Calculations(a, b, operation)
    print(f"The result of {operation} is: {result}")
    if __name__ == "__main__":
        main()