#l=sorted([map(int,input().split)])
l = sorted(map(int, input().split()))
if l[0]+l[1] >l[2]:
    print(1)
else:
    print(0)