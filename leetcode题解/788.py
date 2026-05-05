class Solution:
    def rotatedDigits(self, n: int) -> int:
        #0 1 2 5 6 8 9√ 注意0 1 8
        #3 4 7 x
        r=0
        for i in range(1,n+1):
            a=str(i)
            #if '3' or '4'or '7' in a:
            if '3' in a or '4' in a or '7' in a:
                continue
            c=0
            b=len(a)
            for j in a:
                if j=='0' or j=='1' or j=='8':
                    c+=1
            if c!=b:
                r+=1
        return r
Solution().rotatedDigits(10)