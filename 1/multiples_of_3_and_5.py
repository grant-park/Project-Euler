def find_multiples_of_3_and_5(n):
    sum = 0
    for i in range(0,n):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
    return sum
print(find_multiples_of_3_and_5(1000))
