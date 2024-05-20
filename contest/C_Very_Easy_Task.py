def good(time, x, y, n):

    if time < min(x, y):
        return False

    time -= min(x, y)
    count = (time // x) + (time // y) + 1

    return count >= n


if __name__ == '__main__':

    n, x, y = map(int, input().split())

    l, r = 0, (max(x, y) * n)

    while l + 1 < r:
        mid = l + (r - l) // 2

        if good(mid, x, y, n):
            r = mid
        else:
            l = mid

    print(r)
