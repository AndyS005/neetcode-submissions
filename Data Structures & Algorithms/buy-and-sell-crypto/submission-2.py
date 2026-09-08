class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        total = 0 
        for i in range(len(prices)):
            cur_total = prices[i] - smallest
            if prices[i] < smallest:
                smallest = prices[i]
            if cur_total > total:
                total = cur_total

        return total 
            
                