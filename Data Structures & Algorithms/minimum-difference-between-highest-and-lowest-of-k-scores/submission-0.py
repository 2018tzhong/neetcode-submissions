class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = math.inf
        left = 0
        for idx, val in enumerate(nums):
            if idx - left + 1 == k:
                min_diff = min(min_diff, val - nums[left])
                left += 1
        return min_diff