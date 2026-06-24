class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum %2 != 0:
            return False
        memo = [[0 for i in range(len(nums))] for i in range(total_sum+1)]
        memo_bool = [False for i in range(total_sum+1)]
        nums_set = set()
        for idx, val in enumerate(nums):
            if val in nums_set:
                continue
            nums_set.add(val)
            memo[val][idx] = 1
            memo_bool[val] = True
        for i in range(int(total_sum/2) + 1):
            for j, val in enumerate(nums):
                if i-val > 0 and memo_bool[i-val]:
                    if memo[i-val][j] != 1:
                        memo[i] = memo[i-val].copy()
                        memo[i][j] = 1
                        memo_bool[i] = True
                        break
        # print(memo_bool)
        # print(memo)
        return memo_bool[int(total_sum/2)]
            
