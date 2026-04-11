#超时
#[ 用时: 49m 12s ]
def minimumDistance(nums: list[int]) -> int:
    counts = {}
    r=-1
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    to_del = [k for k, v in counts.items() if v <3]
    for k in to_del:
        del counts[k]
    #counts的键目前为符合条件的数
    if counts=={}:
        return r
    #print(counts)
    for key in counts:
        index = [i for i, x in enumerate(nums) if x == key]
        fast,slow=2,0
        for i in range(len(index)-2):
            d=2*(index[fast]-index[slow])
            if r ==-1 or d <r:
                r=d
            if fast==len(index):
                break
            fast+=1
            slow+=1
    return r
nums=[1,1,2,3,2,1,2]
print(minimumDistance(nums))