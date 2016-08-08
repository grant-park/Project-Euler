import math

def largest_prime_factor(n):
    while True:
        s = smallest_prime_factor(n)
        if s < n:
            n //= s
        else:
            return n
def smallest_prime_factor(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n

print(largest_prime_factor(600851475143))
