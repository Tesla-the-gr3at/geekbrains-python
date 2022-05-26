dividend = int(input("Please enter the number to be divided:"))
divisor = int(input("Please enter the number to be the divisor:"))

def divide_numbers (a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("You can't divide by zero")
        exit(0) 

print(divide_numbers(dividend,divisor))