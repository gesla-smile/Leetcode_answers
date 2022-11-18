class Solution:
    def canJump(self, nums):
        length = len(nums)
        if length == 0:
            return False
        if length == 1:
            return True
        
        most_jump = 0
        for i in range(length):
            if i > most_jump:
                return False
            most_jump = max(most_jump, i + nums[i])
        return True