from decorators import *
def SelectSortv1(list=[],visible=1):#事实上不是选择排序，更像冒泡
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
@timer
def SelectSortv2(list=[],visible=1):
    l=len(list)
    for i in range(l-1):#最后一个元素不需要排序，所以-1
        min=i
        for j in range(i+1,l):
            if list[j]<list[i]:
                min=j
                list[i],list[min]=list[min],list[i]
        if visible:
            print(list)
    return list
def SelectSortv3(list=[],visible=1):
    l=len(list)
    for i in range(l-1):
        for j in range(i+1,l):
            if list[j]<list[i]:
                min_index=j
        if min_index!=i:
            list[i],list[min_index]=list[min_index],list[i]
        if visible:
            print(list)
    return list
if __name__ == '__main__':
    l1=[1,4,7,2,5,8,3,6,9,0]
    print(SelectSortv3(l1))