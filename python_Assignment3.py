#Assignment_3

# Question 1 

def Factorial(n):
     if n < 0:
          return"factorial not defined "
     elif n == 0 :
        return 1
     else:
        N = 1
        for i in range(1,n+1):
            N *= i
        return N

n = int(input("enter a number: "))

factorial = Factorial(n) 

print(f"factorial of {n} = {factorial}")
    
# Question 2 

import math as m 

number = int(input("Enter a number: "))

square_root = m.sqrt(number)
print("square root :", square_root)

logarithm = m.log(number)
print("logarithm :", logarithm)

sine = m.sin(number)
print("sine:",sine)