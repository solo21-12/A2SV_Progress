class Solution:
    def bestClosingTime(self, customers: str) -> int:
        rightSum = customers.count("Y")
        leftSum = 0

        maxPenality = rightSum + leftSum
        ans = 0
        for i in range(1, len(customers)):
            leftSum += 1 if customers[i - 1] == "N" else 0
            rightSum -= 1 if customers[i - 1] == "Y" else 0

            curPenality = leftSum + rightSum
            if curPenality < maxPenality:
                ans = i
                maxPenality = curPenality

        leftSum = customers.count("N")
        curPenality = leftSum + 0

        if curPenality < maxPenality:
            ans = len(customers)

        return ans
