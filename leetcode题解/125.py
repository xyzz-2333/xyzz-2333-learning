class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(char for char in s if char.isalnum()).lower() 
        #不用再写一行s.lower，直接放后面        ↑用isalpha过不去'0p'样例
        a,b=0,len(s)-1
        if len(s)<2:
            return True
        while a<b:
            if s[a]!=s[b]:
                return False
            if s[a]==s[b]:
                a+=1
                b-=1
            #if (len(s)%2==0 and b==a+1) or (len(s)%2==0 and b==a+2):
                #return True            
        return True    
print(Solution.isPalindrome(Solution,'ea'))
