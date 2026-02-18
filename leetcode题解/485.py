class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a,maxa = 0,0
        for i in nums:
            if i == 1: 
                a += 1
                maxa=max(a,maxa)
                
            else:
                a =0
        return maxa