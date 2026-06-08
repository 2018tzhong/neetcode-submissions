class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = set()
        for i in nums:
            if i in once:
                once.discard(i)
            else:
                once.add(i)
        return list(once)[0]