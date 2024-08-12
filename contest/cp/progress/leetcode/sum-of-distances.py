class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        arr = [0] * len(nums)
        count = defaultdict(list)

        for i, num in enumerate(nums):
            count[num].append(i)

        for key, val in count.items():
            if len(val) > 1:
                suffixSum = sum(val)
                preFixSum = 0
                sizeSuffix = len(val)
                sizePrefix = 0
                for num in val:
                    suffixSum -= num
                    preFixSum += num
                    sizeSuffix -= 1
                    sizePrefix += 1

                    arr[num] = (-preFixSum + sizePrefix * num - sizeSuffix * num + suffixSum)

        return arr





        return arr
