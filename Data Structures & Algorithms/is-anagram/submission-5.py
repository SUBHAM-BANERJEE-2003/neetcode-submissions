class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabetmap = [0] * 26
        for i in range(len(s)):
            alphabetmap[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            alphabetmap[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if alphabetmap[i] != 0:
                return False
        return True 
        

        