m, s = map(int, input().split())


def get_max(m, s):
    res = []
    i = 9
    while s and m > 0:
        if s <= i:
            res.append(s)
            s -= s
        else:
            res.append(i)
            s -= i

        m -= 1

    while m > 0:
        res.append(0)
        m -= 1
        
    if m < 0:
        return ([], False)
    elif s > 0:
        return ([], False)


    return (res, True)


def get_min(max):
    res = max[::-1]
    for i in range(len(res)):
        if res[i] > 0:
            res[i] -= 1
            break

    res[0] += 1

    return res


def build_num(nums):
    res = 0
    for num in nums:
        res = res * 10 + num

    return res


maxx, possible = get_max(m, s)
if not possible:
    print(-1, -1)
if s < 1 and m > 1:
    print(-1, -1)
else:
    minn = get_min(maxx)
    print(build_num(minn), build_num(maxx))