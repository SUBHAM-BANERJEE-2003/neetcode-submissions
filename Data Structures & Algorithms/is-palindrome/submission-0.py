class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = ""
        for i in range(len(s)):
            if s[i].isalnum():
                cs += s[i].lower()
        i=0
        j=len(cs) - 1
        while i < j:
            if cs[i] != cs[j]:
                return False
            i += 1
            j -= 1
        return True