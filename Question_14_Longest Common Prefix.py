class Solution:
    def longestCommonPrefix(self, strs):
        
        i = 1
        i_loc = 0
        n_len = len(strs[0])
        while i < len(strs):
            if n_len > len(strs[i]):
                n_len = len(strs[i])
                i_loc = i
                i += 1
            else:
                i += 1
        basic_str = strs[i_loc]
        new_basic_str = basic_str
        
        len_basic = len(basic_str)
        for n in range(0, len_basic):
            for m in range(0, len(strs)):
                if strs[m][n] != basic_str[n]:
                    new_basic_str = basic_str[0:n]
                    return new_basic_str

        return new_basic_str
       