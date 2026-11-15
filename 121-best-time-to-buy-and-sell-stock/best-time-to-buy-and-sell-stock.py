class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for currentprice in prices :
            if currentprice < minprice :
                minprice = currentprice
            else :
                profit = currentprice - minprice
                if profit > maxprofit :
                    maxprofit = profit
        
        return maxprofit
