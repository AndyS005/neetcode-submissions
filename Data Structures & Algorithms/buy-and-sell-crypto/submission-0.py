class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        difference = 0
        for i in range(len(prices)):
            if prices[i] < smallest:
                smallest = prices[i]
                continue
            else:
                if prices[i] - smallest > difference:
                    difference = prices[i] - smallest
        
        return difference
        