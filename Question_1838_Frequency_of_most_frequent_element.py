class Solution:
    def maxFrequency(self, nums, k):
        n = len(nums)
        nums.sort()
        result = 0 
        left = 0
        temp_k = 0

        for right in range(n):
            temp_k += nums[right]
            while temp_k + k < nums[right] * (right - left + 1):
                temp_k -= nums[left]
                left += 1
            result = max(result, right - left + 1)
        
        return result