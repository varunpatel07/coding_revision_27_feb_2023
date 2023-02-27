class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #intitution we can find minimum buy value and max sell value
        maxprofit=0
        minprice=prices[0]
        for i in range(len(prices)):
            minprice=min(minprice,prices[i])
            maxprofit=max(maxprofit,prices[i]-minprice)
        return maxprofit
        