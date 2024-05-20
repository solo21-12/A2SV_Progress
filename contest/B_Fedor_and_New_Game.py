n, m, k = map(int, input().split())
players = []

for _ in range(m + 1):
    players.append(int(input()))


def get_binary(num):
    binary = bin(num)[2:]

    return binary.zfill(32)


def counter(player, fedor, k):
    count = 0
    player = get_binary(player)
    fedor = get_binary(fedor)
    for i in range(32):
        if int(player[i]) ^ int(fedor[i]) == 1:
            count += 1

    return count <= k


count = 0
for player in players[:m]:
    if counter(player, players[-1], k):
        count += 1
        
print(count)
