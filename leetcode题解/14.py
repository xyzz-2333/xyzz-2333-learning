class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=len(strs)
        c=0
        a=strs[0]
        if l==1:
            return strs[0]
        while True:
            for i in strs:
                if i.startswith(a) ==False:
                    pass
                else:
                    c+=1
            if c == l:
                return a
            else:
                a = a[:-1]
                c=0


                