#[ 用时: 3m 59s ]
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l=[0 * i for i in range(len(nums))]
        for i in range(len(nums)):
            l[(i+k)%len(nums)]=nums[i]
        for i in range(len(nums)):
            nums[i]=l[i]
        """
        Do not return anything, modify nums in-place instead.
        """