class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def back_track(left, right):
            if left > right:
                return 0, 0
            
            curr1, nxt1 = back_track(left+1, right)
            curr2, nxt2 = back_track(left, right-1)
                        
            if nums[left] + nxt1 > nums[right] + nxt2:
                return nums[left] + nxt1, curr1
            
            return nums[right] + nxt2, curr2
        
        player1, player2 = back_track(0, len(nums)-1)
        
        return player1 >= player2