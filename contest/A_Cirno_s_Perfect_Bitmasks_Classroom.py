t = int(input())


def find_pos(x) -> int:
    for i in range(32):
        if x & (1 << i) != 0:
            return i
    return 0


def bit_count(n):
    return bin(n).count('1')


def solve(x: int):
    num = 0
    first_one = find_pos(x)
    num |= (1 << first_one)

    if bit_count(x) == bit_count(num):
        for i in range(32):
            if num & (1 << i) == 0:
                num |= (1 << i)
                break

    return num


for _ in range(t):
    x = int(input())
    print(solve(x))
