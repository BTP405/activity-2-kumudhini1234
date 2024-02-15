#def getPrimeNumbers(n):


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    return [i for i in range(2, n+1) if is_prime(i)]

# Example 
n = 20 
prime_numbers = getPrimeNumbers(n)
print(prime_numbers)
