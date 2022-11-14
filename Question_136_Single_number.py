class Solution: #XOR calculation
    def singleNumber(self, nums):
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]   
        return result
