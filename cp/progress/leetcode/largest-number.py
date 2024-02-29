class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        def compare(num1, num2):
            if (num1 + num2) > (num2 + num1):
                return -1
            return 1

        nums = sorted(nums, key=cmp_to_key(compare))
        res = "".join(nums).lstrip("0")

        return res if res else "0"
