class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0 for i in range(len(nums))]
        memo[0] = 1
        max_so_far = 1
        for idx, val in enumerate(nums):
            if idx == 0:
                continue
            max_memo = 1
            for j in range(0, idx):
                if val > nums[j]:
                    max_memo = max(memo[j]+1, max_memo)
            # memo[idx] = max(max_memo, memo[idx-1])
            memo[idx] = max_memo
            max_so_far = max(max_so_far, memo[idx])
        # print(memo)
        return max_so_far