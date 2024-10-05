import math
# Project Euler problem 27. Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

# Initial values

n = 0
a = -999
b = -1000
max_length = 0
product = 0

# Defining the quadratic function
def Q(a, b, n):
   Q =  math.pow(n,2) + a*n + b
   return Q

# Checking primality of a number
def is_prime(n):
    
    if n < 2: 
         return False
    if n % 2 == 0:             
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True
   

for a in range(-999, 999, 1):
 for b in range(-1000, 1000, 1):
   n = 0
   # Checking length of the sequence of consecutive primes produced by Q
   while( is_prime(Q(a,b,n)) == True ):
     n = n + 1

   # Finding the maximum length of a consecutive prime sequence
   if n > max_length:
     max_length = n
     product = a*b

# The product of a and b of the longest consecutive prime sequence
print("The product of a and b of the longest consecutive prime sequence:", product)
#Answer: -59231
   

  
