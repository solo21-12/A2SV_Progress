
def checkPalidrom(s, l):
    N = len(s)
    if l >= N // 2:
        return True
    
    if s[l] != s[N - l - 1]:
        return False
    
    return checkPalidrom(s, l + 1)

    


s = input()
print(checkPalidrom(s, 0))
