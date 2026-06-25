class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # memo = [0 for i in range(amount+1)]

        # for i in coins:
        #     memo[i] = 1
        
        # for i in range(amount+1):
        #     curr_total = memo[i]
        #     for j in coins:
        #         if i-j >= 0:
        #             curr_total += memo[i-j]
        #     memo[i] = curr_total
        # print(memo)

        # return memo[amount]

        n = len(coins)
        memo = [[0 for i in range(amount+1)] for i in range(n+1)]

        for i in range(n+1):
            memo[i][0] = 1
        
        sorted_coins = sorted(coins)
        for idx1 in range(n-1, -1, -1):
            for a in range(amount+1):
                if a - sorted_coins[idx1] >= 0:
                    memo[idx1][a] = memo[idx1+1][a] + memo[idx1][a-sorted_coins[idx1]]

        # print(memo)
        return memo[0][amount]