from collections import Counter
 
 
word = input()
t = int(input())
 
def solve(t, word):
    if len(word) < t:
        return -1
    
    
    count = Counter(word)
    
    if len(count) > t:
        return 0
    
    return t - len(count)
 
 
res = solve(t, word)
if res == -1:
    print("impossible")
else:
    print(res)