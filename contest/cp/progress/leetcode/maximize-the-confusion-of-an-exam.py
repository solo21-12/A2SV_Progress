class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        cons = defaultdict(int)
        l,ans=0,0

        for r in range(len(answerKey)):

            cons[answerKey[r]] += 1

            while r - l + 1 - max(cons["T"],cons["F"]) > k:
                cons[answerKey[l]] -= 1
                l += 1
            

            ans = max(ans, r-l +1)

        return ans
        