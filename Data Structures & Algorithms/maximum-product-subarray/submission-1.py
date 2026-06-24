class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = [0 for i in range(len(nums))]
        neg_memo = [0 for i in range(len(nums))]
        memo[0] = nums[0]
        neg_memo[0] = nums[0]
        max_so_far = -math.inf
        for i in range(1, len(nums)):
            memo[i] = max(nums[i], nums[i]* neg_memo[i-1], nums[i]*memo[i-1])
            neg_memo[i] = min(nums[i], nums[i] * neg_memo[i-1], nums[i] * memo[i-1])
            max_so_far = max(max_so_far, memo[i])
        return max_so_far