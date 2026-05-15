class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        today,b,r=0,prices[0],0
        for i in range(1,len(prices)):
            if prices[i]<b:
                b=prices[i]
                continue
            today=prices[i]-b
            if today>r:
                r=today
        if r>0:return r 
        else: return 0