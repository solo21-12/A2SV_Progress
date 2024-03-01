class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []

        l, r = 0, 0

        while l < len(firstList) and r < len(secondList):
            if (secondList[r][0] <= firstList[l][0] <= secondList[r][1]) or (firstList[l][0] <= secondList[r][0] <= firstList[l][1]):
                start = max(firstList[l][0],secondList[r][0])
                end = min(firstList[l][1],secondList[r][1])
                ans.append([start, end])

                if firstList[l][1] < secondList[r][1]:
                    l += 1
                else:
                    r += 1
            elif firstList[l][0] < secondList[r][0]:
                l += 1
            elif firstList[l][0] > secondList[r][0]:
                r += 1
            else:
                l += 1
                r += 1

        return ans