from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        for i in range(len(nums)):
            j = nums[i]
            if (target-j) in d:
                return [d[target-j], i]
            d[j] = i