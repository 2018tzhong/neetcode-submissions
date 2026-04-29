class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        counts = {}
        for i in nums:
            counts[i] = 0
        for i in nums:
            if i-1 in counts:
                counts[i-1] = 1
        
        # process for checking consecutive chain
        vals_to_check = set()
        for k, v in counts.items():
            if k-1 in counts:
                if v == 0 and counts[k-1] == 1:
                    vals_to_check.add(k)
                    
        print(vals_to_check)
        max_seq = 1
        for val in vals_to_check:
            seq = self.getConsecProcess(counts, val)
            if seq > max_seq:
                max_seq = seq
        return max_seq


    def getConsecProcess(self, counts, num):
        # iterate over dict
        seq = 1
        val = num-1
        while val in counts and counts[val] == 1:
            seq += 1
            val -= 1
        return seq



        