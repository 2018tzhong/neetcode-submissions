class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        memo = [math.inf for i in range(amount+1)]
        coins_set = set()
        for i in coins:
            coins_set.add(i)
            if i < len(memo):
                memo[i] = 1
        # print(memo)
        for i in range(len(memo)):
            for j in coins:
                if j > amount:
                    continue
                if memo[i-j] != -1 and i-j >= 0:
                    memo[i] = min(memo[i], memo[i-j] + 1)
        # print(memo)
        if memo[amount] == math.inf:
            return -1
        return memo[amount]

        