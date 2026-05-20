from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for val, freq in hm.items():
            bucket[freq].append(val)
        for i in range(len(bucket) - 1, -1, -1):
            if len(bucket[i]) > 0:
                for e in bucket[i]:
                    ans.append(e)
            if len(ans) >= k: # may contain multiple elements and exceed k
                return ans
        return ans
        






        


        

        