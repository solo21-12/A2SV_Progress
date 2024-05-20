class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_beggining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def printer(self):

        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        linkedList = ""

        while itr:
            linkedList += str(itr.data) + "-->"
            itr = itr.next

        print(linkedList)


if __name__ == '__main__':
    li = LinkedList()
    li.insert_beggining(3)
    li.insert_beggining(2)

    li.insert_beggining(1)
    li.insert_end(4)

    li.printer()


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        [2,3,1,1,4]
        maxNextAvailableDist =  2
        minSteps = 1
        maxReachableDistance = 4
        '''
        if not nums or len(nums) < 2:
            return 0

        maxReachableDistance, maxNextAvailableDist, minSteps = 0, 0, 0

        for i in range(len(nums)-1):
            # track the max of next index
            maxNextAvailableDist = max(maxNextAvailableDist, i+nums[i])
            if i == maxReachableDistance:  # current index is the furthest we can get, have to do another step to get maxNext
                minSteps += 1

            maxReachableDistance = maxNextAvailableDist

        return minSteps
