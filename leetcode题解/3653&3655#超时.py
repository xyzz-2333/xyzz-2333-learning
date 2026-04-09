#测了几下一次ac，好耶[ 用时: 16m 22s ]
class Solution:
    def xorAfterQueries(self, nums: list[int], queries: List[List[int]]) -> int:
        for i in range(len(queries)):
            idx=queries[i][0]
            while idx<=queries[i][1]:
                nums[idx]=(nums[idx] *queries[i][3]) % (10**9 +7) #(10e9 + 7)
                                                            #↑是浮点数，会卡后面的异或
                idx+=queries[i][2]
        r=0
        for i in range(len(nums)):
            r=r^nums[i]
        return r
#3655其实就是加大了数据规模
#但是看不懂
#反正是hard，以后再说