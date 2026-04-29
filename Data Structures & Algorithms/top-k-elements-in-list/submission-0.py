class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        
        sorted_counts = sorted(counts.items(), key=lambda v: v[1], reverse=True)
        print(sorted_counts)
        return [ki for (ki, v) in sorted_counts[:k]]