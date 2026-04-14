def factorial():
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 
    
    
number = int(input("Enter value of n: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")