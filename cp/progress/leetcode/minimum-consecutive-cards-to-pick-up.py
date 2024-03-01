class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        count = set()
        minLength = float('inf')
        l = 0

        for r in range(len(cards)): 

            while l < len(cards) and cards[r] in count:
                minLength = min(r - l + 1, minLength)
                count.remove(cards[l])
                l += 1

            count.add(cards[r])

        return minLength if minLength != float('inf') else -1




        