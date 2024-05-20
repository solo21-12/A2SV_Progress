x = int(input())


def bit_count(num):
    num = bin(num)[2:]
    return num.count('1')


print(bit_count(x))
