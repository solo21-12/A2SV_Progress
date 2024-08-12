class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([(ticket, i) for i, ticket in enumerate(tickets)] )

        count = 0
        while True:
            count += 1
            ticket, i = queue.popleft()
            ticket -= 1

            if i == k and not ticket:
                return count

            if ticket > 0:
                queue.append((ticket, i))


        return 0
