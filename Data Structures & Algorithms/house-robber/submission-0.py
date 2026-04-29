class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        results = []
        results.append(nums[0])
        results.append(nums[1])
        results.append(nums[0] + nums[2])
        for i in range(3, len(nums)):
            max_val = max(results[i-3], results[i-2])
            results.append(max_val + nums[i])
        return max(results[-1], results[-2])
