# User function Template for python3

import sys
import io
import atexit
import heapq

heapq.heappush

class Solution:
    def swap(self, arr, left, right):
        arr[left], arr[right] = arr[right], arr[left]
    # Heapify function to maintain heap property.

    def heapify(self, arr, n, i):
        larger_child = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[left_child] > arr[larger_child]:
            larger_child = left_child

        if right_child < n and arr[right_child] > arr[larger_child]:
            larger_child = right_child

        if larger_child != i:
            self.swap(arr, larger_child, i)
            self.heapify(arr, n, larger_child)
        # code here

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        for i in range(n // 2, -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        # code here
        self.buildHeap(arr, n)
        for i in range(n - 1, -1, -1):
            self.swap(arr, 0, i)
            self.heapify(arr, i, 0)
        


# {
 # Driver Code Starts
# Initial Template for Python 3

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr, n)
        print(*arr)

# } Driver Code Ends
