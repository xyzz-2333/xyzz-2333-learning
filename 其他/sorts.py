def SelectSortv1(list=[],visible=1):
    l=len(list)
    min=0
    while True:
        for i in range(min,l):
            if list[i] < list[min]:
                list[i],list[min]=list[min],list[i]
        min+=1
        if min==l:
            return list

if __name__ == '__main__':
    l1=[1,4,7,2,5,8,3,6,9,0]
    print(SelectSort(l1))