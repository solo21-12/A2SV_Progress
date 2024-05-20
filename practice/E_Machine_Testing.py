import math

def solve(health, power, n):
    stack = [[power[0], None]]
    total_time = 0
    
    for po, he in zip(power[1:], health[1:]):
        if stack[-1][1] is None:
            res = math.ceil(he / stack[-1][0])
            total_time += res
            stack.append([po, total_time])
        else:
            while stack[-1] != None and po <= 0:
                top = stack[-1]
                cur_dec = top[0] * top[1]
                if cur_dec < po:
                    po -= cur_dec
                    top.pop()
            
            

t = int(input())

for _ in range(t):
    n = int(input())
    health = list(map(int, input().split()))
    power = list(map(int, input().split()))


    ans = solve(health, power, n)
    print(ans)