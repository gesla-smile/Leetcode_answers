class Solution:
    def fourSum(nums, target):
        nums.sort()
        result = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                left = j + 1
                right = n - 1
                remain = target - nums[i] - nums[j]
                while left < right:
                    if nums[left] + nums[right] == remain:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] > remain:
                        right -= 1
                    elif nums[left] + nums[right] < remain:
                        left += 1
        return result

def main():
    test = [1, 0, -1, 0, -2, 2]
    print(Solution.fourSum(test, 0))


main()
