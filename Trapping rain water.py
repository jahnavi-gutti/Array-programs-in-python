#Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

n=int(input())
a = [int(val) for val in input().strip().split(" ")]
w=0
lm=0
rm=0
l=[0]*n
r=[0]*n
for i in range(1,n):
    if a[i-1]>lm:
        lm=a[i-1]
    l[i]=lm
for i in range(n-2,0,-1):
    if a[i+1]>rm:
        rm=a[i+1]
    r[i]=rm
for i in range(1,n-1):
    mlr=min(l[i],r[i])
    if mlr>a[i]:
        w+=mlr-a[i]
print(w)

 
"""
Output:
6
3 0 0 3 2 0 5
10
"""
