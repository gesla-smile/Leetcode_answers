class Solution:
    def intersection(nums1, nums2):
        dict = {}
        res = []
        for i in range(len(nums1)):
            if nums1[i] not in dict:
                dict[nums1[i]] = 1
        for i in range(len(nums2)):
            if nums2[i] in dict:
                res.append(nums2[i])
        final = []
        [final.append(x) for x in res if x not in final]
        return final

nums1 = [1,2,2,1]
nums2 = [2,2]

print(Solution.intersection(nums1, nums2))