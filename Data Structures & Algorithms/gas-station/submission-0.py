class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_gas < total_cost:
            return -1
        
        curr = 0
        start = 0
        found = False
        for i in range(len(gas)):
            curr += gas[i]
            if curr > cost[i]:
                curr -= cost[i]
                if not found:
                    start = i
                    found = True
            else:
                curr = 0
                found = False
        
        return start