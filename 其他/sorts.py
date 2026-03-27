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
@timer
def SelectSortv3(list=[],visible=1):#应该还能优化倒是
    l=len(list)
    for i in range(l-1):
        min_index=i 
        for j in range(i+1,l):
            if list[j]<list[min_index]:
                min_index=j
        if min_index!=i:
            list[i],list[min_index]=list[min_index],list[i]
        if visible:
            print(list)
    return list
def SelectSortv4(arr=None,visible=False):#算是满意的版本
    l=len(arr)
    for i in range(l-1):#最后一个元素不需要排序，所以-1
        min_index = i
        min_value = arr[i]
        for j in range(i + 1, l):
            if arr[j]< min_value:
                min_value=arr[j]
                min_index=j
            if min_index!=i:
                arr[i],arr[min_index]= arr[min_index],arr[i]
            if visible:
                print(arr)
    return arr       
def BubbleSort(arr=None,visible=False): 
    l=len(arr)
    for i in range(l-1):
        for j in range(l-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if visible:
            print(arr)
    return arr       
if __name__ == '__main__':
    l1=[1,4,7,2,5,8,3,6,9,0,12,15,14,13,11,-1,65536]
    #print(SelectSortv2(l1.copy(), visible=0))
    #print(BubbleSort(l1,visible=1))