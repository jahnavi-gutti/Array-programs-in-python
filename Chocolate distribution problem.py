n=int(input())
m=int(input())
a=list(map(int, input().strip().split(" ")))
b=sorted(a)
min=b[-1]
for i in range(n-m):
    dif=b[i+m-1]-b[i]
    if(dif<min):
        min=dif
print(min)
"""
Output:


8
5
3 4 1 9 56 7 9 12
6
"""
