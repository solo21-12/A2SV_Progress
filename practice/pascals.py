from typing import *


def pascal(row, col):
    if row < 0:
        return 0

    if col == 0:
        return 1

    return pascal(row - 1, col) + pascal(row - 1, col - 1)


def pascalGenerate(numRows):

    for i in range(numRows):
        for j in range(i+1):
            print(pascal(i, j), end=" ")

        print()

# print(pascalGenerate(5))


# print(pascal(2,3))


def isSubsetPresent(n: int, k: int, a: List[int]):
    # Write your code here.
    a.sort()

    def checkSubSet(i, k,arr):
        if i >= n:
            if k == 0:
                return True

            return
        
        if k == 0:
            print("loop")
            return True
        
        arr.append(a[i])
        k -= a[i]
        checkSubSet(i + 1, k, arr)

        arr.pop()
        k += a[i]
        checkSubSet(i + 1, k, arr)

        return False


    print(checkSubSet(0, k, []))


isSubsetPresent(5, 3,[1,2,3,4,5])




        

    



