#The idea follows this theorem: http://www.wikihow.com/Determine-the-Number-of-Divisors-of-an-Integer
#is_prime(n) function definition is copied from StackOverflow. In this particular instance the func. is converted to a list
#with prime numbers < sqrt(n)+1
#Idea of this algorithm is to check the amount of prime factors in a given number by calling the is_prime function

# noinspection PyUnresolvedReferences
from math import sqrt

def is_prime(n):
    """"pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2:
         return False;
    if n % 2 == 0:
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

check = 24

def return_factors(m):
    a = int(sqrt(m))+1
    l = []
    for i in range(2,a):
        if is_prime(i) == True:
            l.append(i)
    return l


print(return_factors(6552))


