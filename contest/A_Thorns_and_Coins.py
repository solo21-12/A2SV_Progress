t = int(input())


def solve(paths, n):

    count = 0
    i = 0
    for i in range(len(paths) - 1):
        if paths[i] == '*' and paths[i+1] == "*":
            return count
        elif paths[i] == '@':
            count += 1
        else:
            continue
        
    if paths[-1] == '@':
        count += 1

    return count


for _ in range(t):
    n = int(input())
    paths = (input())
    print(solve(paths, n))
