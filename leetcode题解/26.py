'''class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        r =needle[0]
        for i in range(len(haystack)):
            if len(haystack)-i < len(needle):
                continue
            if haystack[i] ==r:
                for j in range(len(needle)):
                    flag=0
                    if haystack[i+j] != needle[j] :
                        break
                    else:
                        flag+=1
                if flag == len(needle):
                    return i
        return -1
    '''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        r =needle[0]
        ln,lh=len(needle),len(haystack)
        for i in range(lh):
            if i+ln > lh:
                continue
            if haystack[i] ==r:
                flag=0
                for j in range(ln):  
                    if haystack[i+j] != needle[j] :
                        break
                    else:
                        flag+=1
                if flag == ln:
                    return i
        return -1