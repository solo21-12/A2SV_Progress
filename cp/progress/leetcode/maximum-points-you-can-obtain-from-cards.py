class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0,len(cardPoints) - k
        currSum = sum(cardPoints[r:])
        maxScore = currSum

        while r < len(cardPoints):
            currSum += (cardPoints[l] - cardPoints[r])
            maxScore = max(maxScore,currSum)

            l += 1
            r += 1
            

        return maxScore

         

        