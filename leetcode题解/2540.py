class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a,b=0,0
        s1=set(nums1)
        s2=set(nums2)
        #l=min(len(nums1),len(nums2))
        return -1 if len(s1&s2)==0 else min(s1&s2)