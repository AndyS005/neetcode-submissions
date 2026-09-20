class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        total = 0 
        for i in range(len(prices)-1):
            if prices[buy] < prices[sell]:
                total += (prices[sell] - prices[buy])
            buy+=1
            sell+=1

        return total


        