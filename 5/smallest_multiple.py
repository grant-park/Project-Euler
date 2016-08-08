def smallest_multiple(n):
    smallest = 1
    for i in range(11,n+1):
        smallest *= i
    return smallest

print(smallest_multiple(20))


