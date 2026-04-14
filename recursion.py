# This function calculates the nth Fibonacci number using recursion.
## psedocode
 #def fibonacci(n):
#    if n = 0:     
#       return = 0
#     elif n = 1: 
#       return = 1
# else:   
#       return fibonacci(n - 1) + fibonacci(n - 2)
#  end


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 
    
#ACCEPT USER INPUT
number = int(input("Enter the value of n: "))
result = fibonacci(number)
print(f"The {number}th Fibonacci number is: {result}")