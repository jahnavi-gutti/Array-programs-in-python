n=int(input())
arr=[int(x) for x in input().strip().split(" ")]
a=0
b=0
for i in arr:
    a=i
    if i!=b+1:
        print(i-1)
    b=i
"""
Output:
5
1 2 3 5 6
4
"""
