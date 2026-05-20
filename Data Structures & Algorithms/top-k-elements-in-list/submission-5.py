from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        heap = []
        for val, freq in hm.items():
            heap.append((-freq, val))
        heapq.heapify(heap)
        while k:
            freq, val = heapq.heappop(heap)
            ans.append(val)
            k -= 1
        return ans
        






        


        

        