class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        results = [-1 for i in range(10000)]
        for i in intervals:
            for j in range(i[0], i[1]+1):
                if results[j] == -1:
                    results[j] = i[1] - i[0] + 1
                else:
                    results[j] = min(results[j], i[1] - i[0] + 1)
        
        final_results = [results[i] for i in queries]
        return final_results

    
    def intervalLength(self, i):
        return i[1] - i[0] + 1