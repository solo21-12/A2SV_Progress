class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head =None    

    def get_length(self)->int:
        if self.head == None:
            return 0

        itr = self.head
        count = 0

        while itr:
            itr = itr.next
            count += 1

        return count

    def get(self, index: int) -> int:
        if index < 0 or index > self.get_length():
            return -1

        itr = self.head
        while itr and index:
            itr = itr.next
            index -= 1

        return itr.val if itr else -1      

    def addAtHead(self, val: int) -> None:
        node = Node(val,self.head)
        self.head = node    

    def addAtTail(self, val: int) -> None:
        node = Node(val,None)

        if self.head is None:
            self.head = node
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = node   

    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0 or index > self.get_length():
            return -1

        if index == 0:
            next = self.head
            self.head = Node(val,next)
            return

        itr = self.head
        count = 0

        while itr:

            if count == index - 1:
                next = itr.next
                itr.next = Node(val,next)
                break

            count += 1
            itr = itr.next
  
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.get_length():
            return -1

        if index == 0 and self.head:
            self.head = self.head.next
            return

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                if itr.next:
                    itr.next = itr.next.next
                else:
                    itr.next = None
                break
                
            count += 1
            itr = itr.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)