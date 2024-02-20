class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        index = deque(range(N))
        ans = [None] * N
        deck.sort()

        for card in deck:
            ans[index.popleft()] = card

            if index:
                index.append(index.popleft())

        return ans

        