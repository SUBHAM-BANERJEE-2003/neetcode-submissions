class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxl = 0
        mp = {}
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            maxl = max(maxl, r - l + 1)
        return maxl

