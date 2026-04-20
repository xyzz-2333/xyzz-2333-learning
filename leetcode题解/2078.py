class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l = len(colors)
        r = 0
        for i in range(l):
            if colors[i] != colors[-1]:
                r = max(r,max(i,l-i-1))
        return r