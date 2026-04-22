#[ 用时: 14m 16s ]
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        c=0
        r=[]
        for q in queries:
            for i in range(len(dictionary)):
                    c=0
                    for j in range(len(q)):
                        if q[j] != dictionary[i][j]:
                            c+=1
                    if c<=2:
                        r.append(q)
                        break
        return r