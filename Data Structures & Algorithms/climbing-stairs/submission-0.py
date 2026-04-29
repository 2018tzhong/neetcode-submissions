class Solution:
    def climbStairs(self, n: int) -> int:
        results = []
        results.append(1)
        results.append(1)

        for i in range(2, n+1):
            results.append(results[i-1] + results[i-2])

        return results[n]