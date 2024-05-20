#User function Template for python3

from collections import defaultdict, deque

class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        charcter = set()
        graph = defaultdict(list)
        inorder = defaultdict(int)
        
        for i in range(N - 1):
            word1, word2 = alien_dict[i], alien_dict[i + 1]
            l = min(len(word1), len(word2))
            
            for i in range(l):
                if word1[l] != word2[l]:
                    graph[word1[l]].append(word2[l])
                    inorder[word2[l]] += 1
                    break
                    
            
            charcter.update(word1)
            charcter.update(word2)
            
        q = deque()
        vis= set()
        
        for ch in charcter:
            if ch not in inorder:
                q.append(ch)
                vis.add(ch)
                
        result = []
        while q:
            node = q.popleft()
            result.append(node)
            
            if node in graph:
                for nbr in graph[node]:
                    if nbr in inorder and nbr not in vis:
                        inorder[nbr] -= 1
                        
                        if inorder[nbr] == 0:
                            q.append(nbr)
                            vis.add(nbr)
        return result
            
    
            
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends