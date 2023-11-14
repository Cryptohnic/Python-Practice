# Brandon Alexander 9/5/23

import math

# returns true if the number is only divisible by itself and 1
def is_prime(number:int) -> bool:
    end=int(math.sqrt(number))+1
    for i in range(2,end): # loop up to and including the square root of the number and if no divisors yet, it is prime
        if number%i==0:
            return False
    return True

# returns true if the numbers share no factors other than 1
def are_relatively_prime(num1:int,num2:int) -> bool:
    # if is_prime(num1) and is_prime(num2): return True
    smallerNum=num1 if num1<num2 else num2
    for i in range(smallerNum,1,-1): # loop down to one and if don't share divisors then relatively prime
        if num1%i==0 and num2%i==0:
            return False
    return True

# returns a list of all primes less than or equal to the input
def primes(number:int) -> list:
    list=[]
    for i in range(2,number+1): # loop through all numbers that are <= prime and add to list if prime
        if is_prime(i):
            list.append(i)
    return list

# returns a representation of the input that has been output as a list of prime factors that multiply together to create itself
def prime_decomposition(number:int) -> list:
    # if is_prime(number):
    #     return [number]
    list=[]
    primeslist=primes(number)
    for prime in primeslist: # loop through each prime and add it to the list until it doesn't fit into number anymore
        while number%prime==0:
            number//=prime
            list.append(prime)
        if number==0: break
    return list

# run the code
def main():
    print(is_prime(8))
    print(is_prime(2))
    print(is_prime(3))
    print(is_prime(11))
    print(is_prime(103))
    print('\n\n\n')
    print(are_relatively_prime(1,2))
    print(are_relatively_prime(2,2))
    print(are_relatively_prime(1,3))
    print(are_relatively_prime(10,4))
    print('\n\n\n')
    print(primes(1))
    print(primes(2))
    print(primes(3))
    print(primes(4))
    print(primes(5))
    print(primes(6))
    print(primes(7))
    print(primes(8))
    print(primes(9))
    print(primes(10))
    print(primes(11))
    print('\n\n\n')
    print(prime_decomposition(1))
    print(prime_decomposition(2))
    print(prime_decomposition(3))
    print(prime_decomposition(4))
    print(prime_decomposition(5))
    print(prime_decomposition(6))
    print(prime_decomposition(7))
    print(prime_decomposition(8))
    print(prime_decomposition(9))
    print(prime_decomposition(10))
    print(prime_decomposition(11))
    print(prime_decomposition(12))
    print(prime_decomposition(13))
    print(prime_decomposition(14))
    print(prime_decomposition(15))
    print(prime_decomposition(16))
    print(prime_decomposition(17))
    print(prime_decomposition(18))
    print(prime_decomposition(19))
    print(prime_decomposition(20))
    print(prime_decomposition(22))
    print(prime_decomposition(23))

if __name__=='__main__':
    main()