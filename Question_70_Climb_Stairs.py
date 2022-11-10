# Soltion 1
# 这里使用的排列组合的思想
# import math
# class Solution:
#     def climbStairs(n):
#         res = 0
#         start = n
#         for m in range(0, n//2+1):
#             res += math.comb(start,m)
#             start = start - 1

#         return res

# Solution 2 
#f(x) = f(x-1)+f(x-2) 这里使用的是斐波拉切数列

class Solution:
    def climbStairs(self, n):
        a = 1
        b = 2
        i = 3
        if n == a: return a
        if n == b: return b

        while i <= n:
            c = a + b
            a = b
            b = c
            i = i + 1
        
        return c