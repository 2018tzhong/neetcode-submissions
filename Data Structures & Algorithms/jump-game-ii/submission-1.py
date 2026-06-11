class Solution:
    def jump(self, nums: List[int]) -> int:
        
        results = [math.inf for i in range(len(nums))]
        results[-1] = 0
        for idx in range(len(nums)-2, -1, -1):
            r = min(len(nums)-1, idx + nums[idx])
            min_el = math.inf
            for j in range(idx+1, r+1):
                min_el = min(results[j], min_el)
            # print(idx, r, min_el)
            results[idx] = 1 + min_el
        # print(results)
        return results[0]