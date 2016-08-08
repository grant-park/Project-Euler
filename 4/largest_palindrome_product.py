def largest_palindrome_product():
    largest = (0,0)
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            prod = i*j
            strp = str(prod)
            if (strp[0] == strp[-1]):
                if len(strp)%2 == 0:
                    arr = magic2(prod) 
                    mid = len(arr)//2
                    reversed = arr[mid:]
                    reversed.reverse()
                    if arr[:mid] == reversed and i*j > largest[0]*largest[1]:
                      largest = (i,j) 
                else:
                    arr = magic2(prod) 
                    mid = len(arr)//2
                    reversed = arr[mid:]
                    reversed.reverse()
                    if arr[:mid] == reversed and i*j > largest[0] * largest[1]:
                        largest = (i,j)
    print(largest)


def magic2(num):
    return [int(i) for i in str(num)]

largest_palindrome_product()
