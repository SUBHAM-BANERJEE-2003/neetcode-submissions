class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        c1 = {}
        c2 = {}
        for c in t:
            c1[c] = 1 + c1.get(c,0)
        have, need = 0, len(c1)
        res, resl = [-1,-1], float('inf')
        l = 0
        for r in range(len(s)):
                c2[s[r]] = 1 + c2.get(s[r],0)
                if s[r] in c1 and c2[s[r]] == c1[s[r]]:
                    have += 1
                while need == have:
                    if r - l + 1 < resl:
                        resl = r - l + 1
                        res = [l, r]
                    c2[s[l]] -= 1
                    if s[l] in c1 and c2.get(s[l],0) < c1[s[l]]:
                        have -= 1
                    l += 1
        return s[res[0] : res[1]+1] if resl < float('inf') else ""

        