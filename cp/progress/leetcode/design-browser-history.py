class ListNode:
    def __init__(self,prev_node,next_node,url):
        self.prev_node = prev_node
        self.next_node = next_node
        self.url = url

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(None,None,homepage)
        self.currNode = self.head
        

    def visit(self, url: str) -> None:
        self.currNode.next_node = ListNode(self.currNode,None,url)
        self.currNode = self.currNode.next_node
        

    def back(self, steps: int) -> str:
        while steps and self.currNode.prev_node:
            self.currNode = self.currNode.prev_node
            steps -= 1

        return self.currNode.url
        

    def forward(self, steps: int) -> str:
        while steps and self.currNode.next_node:
            self.currNode = self.currNode.next_node
            steps -= 1

        return self.currNode.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)