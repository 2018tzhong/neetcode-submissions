class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        q = [([], 0)]
        results = set()
        while q:
            els, curr_sum = q.pop()
            if curr_sum > target:
                continue
            elif curr_sum == target:
                results.add(tuple(sorted(els)))

            for i in nums:
                if curr_sum + i <= target:
                    q.append((els + [i], curr_sum + i))
        return [list(i) for i in list(results)]
