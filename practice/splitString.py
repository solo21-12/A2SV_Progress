from typing import List


s = "055043"
N = len(s)


def backtrack(idx, path: List):
    
    if idx >= N:
        for i in range(1, len(path)):
            if path[i - 1] - path[i] != 1:
                return False

        return len(path) >= 2

    for j in range(idx, N):
        val = int(s[idx:j+1])
        path.append(val)

        if backtrack(j + 1, path):
            return True
        path.pop()

    return False
