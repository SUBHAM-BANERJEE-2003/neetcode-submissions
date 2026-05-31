class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = [0] * 26
        c2 = [0] * 26
        if len(s1) > len(s2):
            return False
        # for first window
        for i in range(len(s1)):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1
        if c1 == c2:
            return True
        #now slide the window
        l = 0
        for r in range(len(s1), len(s2)):
            c2[ord(s2[r]) - ord('a')] += 1
            c2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if c1 == c2:
                return True
        return False