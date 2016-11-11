import itertools

"""
 The sum of an arithmetic progression is N(F + L)/2 where N represents the number of elements to be summed, F is the first element of the series to be summed, and L is the last element of the series to be summed.
 A = Sum of 3 + 6 + ... + 999 = 333(3 + 999)/2
 B = Sum of 5 + 10 + ... + 995 = 199(5 + 995)/2
 C = Sum of 15 + 30 + ... + 990 = 66(15 + 990)/2
 Sum of multiples of 3 or 5 below 1000 = A + B - C
"""

print (333*(3 + 999)/2 + 199*(5 + 995)/2 - 66*(15 + 990)/2)

# generalizing
def sum_mult(below,*multiples_of):
    # if all multiples are >= the constraint
    if len(list(filter(lambda x: x >= below, multiples_of))) == len(multiples_of):
        return 0

    # auxillary for progression sum
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
