from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            am = [0] * 26
            for c in s:
                am[ord(c) - ord('a')] += 1
            hm[tuple(am)].append(s)

        return list(hm.values())


        