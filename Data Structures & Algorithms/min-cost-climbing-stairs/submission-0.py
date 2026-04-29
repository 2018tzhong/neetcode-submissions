class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        result_costs = []
        result_costs.append(cost[0])
        result_costs.append(cost[1])
        for i in range(2, len(cost)):

            result_costs.append(min(result_costs[i-1], result_costs[i-2])+cost[i])

        return min(result_costs[-1], result_costs[-2])
    
        