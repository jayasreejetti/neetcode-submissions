class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit=prices[j]-prices[i]
                maxi=max(maxi,profit)
        return maxi

        