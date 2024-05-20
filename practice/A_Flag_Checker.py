n,m = map(int, input().split())


cur_sum = -1
nums = []
for _ in range(n):
    nums.append(input())

   
def cal_sum2(word):
    first = word[0]
    n = len(word)
    
    cur_sum = n * int(first)
    
    return cur_sum 
   
def cal_sum(word):
    sum = 0
    for ch in word:
        sum += int(ch)
    return sum
 
def solve(nums):
    prev = -1
    
    for word in nums:
        cur_sum = cal_sum(word)
        right = cal_sum2(word)
        
        if cur_sum != right:
            return False    
        if prev != -1:
            if cur_sum == prev:
                return False
        
        prev = cur_sum
        
    return True


if solve(nums):
    print("YES")
else:
    print("NO")
            
    
    
    