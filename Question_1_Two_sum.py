# Solution 1
import copy
class Solution:
    def twoSum(nums, target):
        temp_nums = copy.deepcopy(nums)
        temp_nums.sort()
        first_pointer = 0 
        sec_pointer = len(temp_nums)-1

        while temp_nums[first_pointer] + temp_nums[sec_pointer] != target:
            if temp_nums[first_pointer] + temp_nums[sec_pointer] > target:
                sec_pointer -= 1
            elif temp_nums[first_pointer] + temp_nums[sec_pointer] < target:
                first_pointer += 1

        a = nums.index(temp_nums[first_pointer])
        nums[a] = None
        b = nums.index(temp_nums[sec_pointer])
        return [a,b]


# Solution 2
class Solution:
    def twoSum(self, nums, target):
        dct = {}
        for i, n in enumerate(nums):
            cp = target - n
            if cp in dct:
                return [dct[cp], i]
            else:
                dct[n] = i