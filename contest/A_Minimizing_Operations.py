t = int(input())

def solve():
    n = int(input())

    nums = list(map(int,input().split()))

    largest = max(nums)
    smallest = min(nums)

    return largest - smallest


for _ in range(t):
    print(solve())