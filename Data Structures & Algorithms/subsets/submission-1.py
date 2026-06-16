class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        for num in nums:
            results = results + [subset + [num] for subset in results]
        
        return results