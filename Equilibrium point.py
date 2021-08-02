#Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
#Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.
n=int(input())
l=list(map(int,input().split(" ")))
rs=0
ls=0
p=-1
for i in range(0,n):
    rs+=l[i]
for i in range(0,n):
    rs-=l[i]
    if ls==rs:
        p=i+1
        break
    ls+=l[i]
print(p)
"""
Output:
7
1 2 3 6 1 1 4
4
"""
