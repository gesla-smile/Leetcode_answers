class Solution:
    def romanToInt(self, s: str) -> int:
        dict={'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        i = 0 
        while i < len(s)-1:
            if dict[s[i]] >= dict[s[i+1]]:
                result += dict[s[i]]
                i = i + 1
            else:
                result += (dict[s[i+1]] - dict[s[i]])
                i = i + 2
        if len(s) >= 2:
            if dict[s[-2]] >= dict[s[-1]]:
                result += dict[s[-1]]
        elif len(s) == 1:
            result = dict[s[-1]]

        return result