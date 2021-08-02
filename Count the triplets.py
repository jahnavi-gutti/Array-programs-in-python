#Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element
n=int(input())
a=list(map(int, input().strip().split(" ")))
Count=0
for i in range(n):
    for j in range(i+1,n):
        if  a[i]+a[j] in a:
            Count+=1

print(Count)
"""
Output1:
3
2 3 4
0
Output2;
5 
1 5 3 2 6
3
"""
