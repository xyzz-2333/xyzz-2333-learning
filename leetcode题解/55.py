class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums)==1:
            return True
        if 0 not in nums:
            return True
        else:
            for i in range(len(nums)-1,-1,-1):
                if nums[i]==0:
                    if i == len(nums)-1:
                        continue                    
                    f=0
                    for j in range(i-1,-1,-1):
                        if nums[j]>i-j:
                            f=1
                            break
                    if f==0:
                        return False
        return True
Solution.canJump(Solution(),[2,5,0,0])
Solution.canJump(Solution(),[2,0,0])