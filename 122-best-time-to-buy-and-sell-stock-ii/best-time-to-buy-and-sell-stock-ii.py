class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #prices = [7, 1, 5, 3, 6, 4]
        buy = float('inf')
        profit = 0

        for price in prices:
            if buy >= price:
                buy = price
            else:
                profit += (price - buy)
                buy = price
        
        return profit
