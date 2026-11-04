class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < best:
                best = prices[i]
            else:
                profit = max(prices[i] - best, profit)
        
        return profit