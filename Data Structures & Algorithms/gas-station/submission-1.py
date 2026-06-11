class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_cost > total_gas:
            return -1
        
        # gas   5 1 1 4 4
        # cost  1 3 7 1 1
        # does doing this after the biggest negative differential make sense?
        largest_neg_diff_idx = 0
        largest_neg_diff = 0
        eligible_idx = set()
        for idx, val in enumerate(gas):
            diff = val - cost[idx]
            if diff >= 0:
                eligible_idx.add(idx)
        
        for i in eligible_idx:
            check = self.checkCanCompleteCircuit(gas, cost, i)
            if check:
                return i
        
        return -1

    def checkCanCompleteCircuit(self, gas, cost, starting_idx):
        curr_gas = 0
        for i in range(starting_idx, len(gas)):
            curr_gas += gas[i]
            curr_gas -= cost[i]
            if curr_gas < 0:
                return False

        for i in range(0, starting_idx):
            curr_gas += gas[i]
            curr_gas -= cost[i]
            if curr_gas < 0:
                return False
        return True
    