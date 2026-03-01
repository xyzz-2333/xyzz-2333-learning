class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l=[]
        def skip(list):
            list.append("Push")
            list.append("Pop")
        for i in range(1,target[-1]+1):
            if i in target:
                l.append("Push")
            else:
                skip(l)
        return l