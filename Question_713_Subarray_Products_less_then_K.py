class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        L = len(nums)
        left = 0 
        right = 0
        prodct = 1
        result = 0
        while right < L:
            prodct *= nums[right]
            while prodct >= k and left <= right:
                prodct /= nums[left]
                left += 1
            result += right - left + 1
            right += right + 1
        return result
