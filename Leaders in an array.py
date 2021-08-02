n=int(input())
l=list(map(int,input().split(" ")))
m=-1
l1=[]
for i in range(len(l)-1,-1,-1):
    if l[i]>m:
        m=l[i]
        l1.append(m)
    le=len(l1)
for i in range(le-1,-1,-1):
    print(l1[i],end=" ")
"""
Output:
6
16 17 4 3 5 2
17 5 2
"""
