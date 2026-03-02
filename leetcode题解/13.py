#方法1
class Solution:
    def romanToInt(self, s: str) -> int:
        r=0
        for i in range(len(s)):
            if i==len(s)-1:
                if s[i]=='I':
                    r += 1
                elif s[i]=='X':
                    r += 10
                elif s[i]=='C':
                    r += 100
                elif s[i] == 'L':
                    r += 50
                elif s[i] == 'V':
                    r += 5
                elif s[i] == 'D':
                    r += 500
                elif s[i] == 'M':
                    r += 1000
                continue
            else:
                if s[i]=='I' :
                    if  (s[i+1]=='V' or s[i+1]=='X'):
                        r -= 1
                    else:
                        r += 1
                if s[i]=='X':
                    if (s[i+1]=='L' or s[i+1]=='C'):
                        r -= 10
                    else:
                        r += 10
                if s[i]=='C':
                    if (s[i+1]=='D' or s[i+1]=='M'):
                        r -= 100
                    else:
                        r += 100
            if s[i]=='V':
                r+=5
            if s[i]=='L':
                r+=50  
            if s[i]=='D':
                r+=500
            if s[i]=='M':
                r+=1000
        return r         
        '''
        for i in range(len(s)):
            if s[i]=='I' and (s[i+1]=='V' or s[i+1]=='X'):
                continue
            if i>0 and (s[i]=='V' or s[i]=='X') and s[i-1]=='I':
                if s[i]=='V':
                    r+=4
                elif s[i]=='X':
                    r+=9
            
'''
#方法2,为什么跑不通呢？
class Solution:
    def romanToInt(self, s: str) -> int:
        def VLDM(ch):
            r=0
            if ch=='V':
                r+=5
            if ch=='L':
                r+=50  
            if ch=='D':
                r+=500
            if ch=='M':
                r+=1000
            return r
        r=0
        for i in range(len(s)):
            if i==len(s)-1:
                if s[i]=='I':
                    r += 1
                elif s[i]=='X':
                    r += 10
                elif s[i]=='C':
                    r += 100
                elif s[i] == 'L':
                    r += 50
                elif s[i] == 'V':
                    r += 5
                elif s[i] == 'D':
                    r += 500
                elif s[i] == 'M':
                    r += 1000
                continue
            else:
                if s[i]=='I' :
                    if  (s[i+1]=='V' or s[i+1]=='X'):
                        r -= 1
                    else:
                        r += 1
                if s[i]=='X':
                    if (s[i+1]=='L' or s[i+1]=='C'):
                        r -= 10
                    else:
                        r += 10
                if s[i]=='C':
                    if (s[i+1]=='D' or s[i+1]=='M'):
                        r -= 100
                    else:
                        r += 100
                r+=VLDM(i)
        return r