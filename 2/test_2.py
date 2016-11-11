def even_fibonacci_numbers(n):
    sum = 0
    x = 1
    y = 2
    while x <= n:
        if x % 2 == 0:
            sum += x
        x, y = y, x + y
    return sum
print(even_fibonacci_numbers(4000000))
