from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sl = SortedList()
        results = []
        l = 0
        for r, num in enumerate(nums):
            sl.add(num)
            if r-l >= k:
                sl.remove(nums[l])
                l+=1
            if r-l == k-1:
                results.append(sl[-1])
        return results
