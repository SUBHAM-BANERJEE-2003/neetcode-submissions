class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        most_common_elements =  Counter(nums).most_common(k)
        for e in most_common_elements:
            l.append(e[0])
        return l

        