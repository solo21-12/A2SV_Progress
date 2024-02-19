class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for i, ticket in enumerate(tickets):
            queue.append((ticket, i))

        count = 0
        while True:
            count += 1
            ticket, i = queue.popleft()
            ticket -= 1
            print(ticket, i)

            if ticket > 0:
                queue.append((ticket, i))
            
            if i == k and not ticket:
                return count

        return 0



        