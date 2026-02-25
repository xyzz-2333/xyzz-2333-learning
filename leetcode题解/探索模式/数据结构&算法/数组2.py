class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a=sum(nums)
        seted=sum(set(nums))
        r=a-seted
        c = 0
        for i in range(1, len(nums)+1):
            c += i
        return [r,c-seted]
'''       
        a=sorted(nums)
        if len(a)==2:
            if a[1]==1:
                return [1,2]
            else: return [2,1]
        if a[1]== a[2]:
            return [2,1]
        for i in range(len(a)):

            if len(a)==2 and a[i]==a[i+1] and a[i]==2:
                return [2,1]

                #气抖冷，凭什么【2,2】的结果不是【2,3】
                #行吧我知道了 
            if a[i]==a[i+1]:
                return [a[i],a[i]+1]'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        r = []
        for i in nums:
            c = 0
            for j in nums:
                if j < i:
                    c += 1
            r.append(c)
        return r

'''
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list=[]
        c=0
        for i in nums:
            for j in nums:
                if j < i:
                    c+=1
                    list.append(c)
                c=0
        return list
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=len(nums)
        s=set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in s]
            