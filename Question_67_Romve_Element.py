class Solution:
    def removeElement(self, nums, val: int) -> int:
        pointer = 0
        while pointer<len(nums):
            if nums[pointer] == val:
                nums.remove(nums[pointer])
            else:
                pointer += 1
        return len(nums); nums