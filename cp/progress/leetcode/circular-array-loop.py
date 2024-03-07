class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)

        def nextPostion(i, forward):
            curDir = nums[i] > 0

            if curDir != forward:
                return -1

            nextPos = (i + nums[i]) % N
            if nextPos == i:
                return -1

            return nextPos

        for i in range(N):
            slow, fast = i, i
            forward = nums[i] > 0

            while True:
                slow = nextPostion(slow, forward)
                if slow == -1:
                    break

                fast = nextPostion(fast, forward)
                if fast == -1:
                    break

                fast = nextPostion(fast, forward)
                if fast == -1:
                    break

                if fast == slow:
                    return True

        return False
