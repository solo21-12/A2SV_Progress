def solve(s, pos):
    N= len(s)
    stack = []
    
    for ch in s:
        while stack and stack[-1] > ch:
            pos -= (N - 1)
            stack.pop()
            
        if pos < len()
            