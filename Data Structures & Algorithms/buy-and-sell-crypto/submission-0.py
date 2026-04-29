class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find min to left

        min_left = [math.inf for i in range(len(prices))]
        for i in range(1, len(prices)):
            min_left[i] = min(prices[i-1], min_left[i-1])

        max_profit = 0
        for j in range(len(prices)):
            max_profit = max(prices[j]-min_left[j], max_profit)

        return max_profit