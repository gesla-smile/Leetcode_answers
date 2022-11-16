class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_list = []
        for i in range(len(s)):
            temp_list.append(s[i])
            if s[i].isupper():
                temp_list[i] = temp_list[i].lower()
        s = ''.join(filter(str.isalnum, temp_list))
        return s == s[::-1]

s = "A man, a plan, a canal: Panama"

def main():
    print(Solution.isPalindrome(s))

main()