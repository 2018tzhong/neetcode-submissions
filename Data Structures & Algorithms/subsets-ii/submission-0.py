class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = set()
        nums.sort()

        def dfs(idx, curr):
            results.add(tuple(curr))

            if idx >= len(nums):
                return
            
            curr.append(nums[idx])
            dfs(idx+1, curr)
            curr.pop()
            dfs(idx+1, curr)

        dfs(0, [])
        return [list(i) for i in list(results)]