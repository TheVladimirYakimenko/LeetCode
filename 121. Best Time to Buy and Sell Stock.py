class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        if prices:
            cur_min = prices[0]

            for idx in range(1, len(prices)):
                if prices[idx] < cur_min:
                    cur_min = prices[idx]
                elif prices[idx] - cur_min > max_profit:
                    max_profit = prices[idx] - cur_min
            
        return max_profit