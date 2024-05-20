from collections import defaultdict


def find_child(arr, current):
    parent = current
    child_left = (parent * 2) - 1
    child_right = (parent * 2) - 2

    if arr[child_left] < arr[child_right]:
        return child_left
    else:
        return child_right


def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]


def heappop(heap):
    if not heap:
        return None
    min_value = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    current = 0
    heapify_down(heap, len(heap), current)
    return min_value


def heapify_down(arr, n, current):
    child = find_child(arr, current)

    while arr[child] > arr[current] and child < n - 1:
        swap(arr, child, current)

        current = child
        child = find_child(arr, current)


def test():
    heap = [2, 4, 5, 7, 9, 10]
    min_val = heappop(heap)
    assert min_val == 2, f"Error: expected 2, but got {min_val}"
    assert heap == [4, 7, 5, 10,
                    9], f"Error: expected [4, 7, 5, 10, 9], but got {heap}"

    heap = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    min_val = heappop(heap)
    assert min_val == 1, f"Error: expected 1, but got {min_val}"
    assert heap == [2, 4, 3, 8, 5, 6, 7,
                    9], f"Error: expected [2, 4, 3, 8, 5, 6, 7, 9], but got {heap}"

    print("Great Job !!!")


test()




class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        adj = defaultdict(list)
        
        for word in alien_dict:
            for i in range(1, len(word)):
                adj[word[i]].append(word[i - 1])
                
                
        
        def dfs(node):
            vis.add(node)
            
            for neigbour in adj[node]:
                if neigbour not in vis:
                    dfs(neigbour)
                    
            result_stack.append(node)
            
        vis = set()
        result_stack = []
        
        print(result_stack)
        
        return []
    
    