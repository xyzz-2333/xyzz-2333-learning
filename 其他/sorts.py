def SelectSortv1(list=[],visible=1):
    #事实上不是选择排序，更像冒泡
    l=len(list)
    min=0
    while True:
        for i in range(min,l):
            if list[i] < list[min]:
                list[i],list[min]=list[min],list[i]
        if visible:
            print(list)
        min+=1
        if min==l:
            return list
def SelectSortv2(list=[],visible=1):
    l=len(list)
    for i in range(l):
        min
        for j in range(i,l):
            if list[j]<list[i]:
                min=list[j]
                list[i],list[min]=list[min],list[i]
        if visible:
            print(list)
    return list
if __name__ == '__main__':
    l1=[1,4,7,2,5,8,3,6,9,0]
    print(SelectSortv2(l1))