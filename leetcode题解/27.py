class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0  
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
'''
#改的是局部变量所以跑不通
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for items in nums:
            if items == val:
                items=''
                i=i+1
        nums=sorted(nums)
        return len(nums)-i

        '''