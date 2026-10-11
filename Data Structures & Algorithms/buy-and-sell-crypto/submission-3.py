class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        total = 0
        for price in prices:
            smallest = min(smallest, price)
            total = max(total, price - smallest)

        return total

            
                