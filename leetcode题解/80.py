class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic={}
        for i in range(len(nums)-1,-1,-1):
            if nums[i] not in dic.keys():
                dic[nums[i]]=1
            else:dic[nums[i]]+=1
            if dic[nums[i]]>2:
                nums.pop(i)
                