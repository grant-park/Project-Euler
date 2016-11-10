import itertools

# Sum of any arithmetic progression is N(n1 + nN)/2 where N represents the number of elements to be summed, n1 is the first element of the series to be summed, and nN is the last element of the series to be summed.

# A = Sum of 3 + 6 + ... + 999 = 333(3 + 999)/2
# B = Sum of 5 + 10 + ... + 1000 = 199(5 + 995)/2
# C = Sum of 15 + 30 + ... + 995 = 66(15 + 990)/2
# Sum of multiples of 3 or 5 below 1000 = A + B - C

print (333*(3 + 999)/2 + 199*(5 + 995)/2 - 66*(15 + 990)/2)

# let's generalize this solution as a function to solve similar problems

def sum_mult(below,*multiples_of):
    # handle edge case in which all the multiples are actually >= the constraint
    if len(list(filter(lambda x: x >= below, multiples_of))) == len(multiples_of):
        return 0

    # auxillary fx for finding the sum of an arithmetic progression
    def aux_ap(first):
        last = 0
        i = below - 1
        while i != 0:
            if i%first == 0:
                last = i 
                i = 0
            else:
                i -= 1
        num = last/first
        return (last + first)*num/2

    intersection = list(map(lambda x: aux_ap(x[0]*x[1]), itertools.combinations(multiples_of,2)))
    union = list(map(lambda x: aux_ap(x),multiples_of))
    return sum(union) - sum(intersection)

print sum_mult(1000,3,5)
