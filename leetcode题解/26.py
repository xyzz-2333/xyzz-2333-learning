class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a= sorted(set(nums))
        l=len(a)        
        for i in range(l):
            nums[i] = a[i]
        return l