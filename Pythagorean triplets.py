import numpy as job
n=int(input())
a=list(map(int, input().strip().split(" ")))
for i in range(len(a)):
    arr1 = job.sqrt(a)
count=0
for i in range(n):
    for j in range(i+1,n):
        if  a[i]**a[i]+a[j]**a[j] in arr1:
            count+=1
if(count>=0):
    print("yes")
else:
    print("no")
"""    
Output:
5
3 2 4 6 5
Yes
"""
