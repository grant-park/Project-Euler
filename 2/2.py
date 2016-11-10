# Fib seq is 1,2,3,5,8,13,...
# Notice the even numbers 2,8,34,144,610,...
# 8 is 4*2 + 0
# 34 is 4*8 + 2
# 144 is 4*34 + 8
# 610 is 4*144 + 34

# The constant being added to 4*previous_term is the 2nd to previous, even fibonacci term.
# We'll use 2 and 8 for our base case and inductively bruteforce the sequence until 4 million

def fib(n):
    if n == 1:
        return 2
    elif n == 2:
        return 8
    else:
        return 4*fib(n-1) + fib(n-2)

sum = 0
n = 1
while sum < 4000000:
    sum += fib(n)
    n += 1
print(sum)
