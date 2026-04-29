class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        results = []
        # print(sorted_nums)
        for i in range(len(sorted_nums)):
            adj_target = -1 * sorted_nums[i]
            adj_m = {}
            # print(i, adj_target)
            for j in range(i+1, len(sorted_nums)):
                if (sorted_nums[j]) in adj_m.keys():
                    # add this to results
                    # print(i, j, adj_target, sorted_nums[j], adj_m)
                    results.append((-adj_target, sorted_nums[j], adj_m[sorted_nums[j]]))
                else:
                    adj_m[adj_target-sorted_nums[j]] = sorted_nums[j]
                
        unique_results = list(dict.fromkeys(results))
        return unique_results

        
