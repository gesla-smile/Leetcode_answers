class Solution:
    def isValid(self, s):
        dict = {"(":1,")":2,"[":3,"]":4,"{":5,"}":6 }
        stack = []
        n = 1
        if s == stack:
            return True
        if len(s) == 1:
            return False

        for elem in s:
            stack.append(elem)
            if len(stack) > 1:
                if dict[stack[-2]]+1 == dict[stack[-1]]:
                    stack.pop()
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
