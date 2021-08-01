n=int(input())
a=[int(x) for x in input().strip().split(" ")]
count=0
for i in range(n):
    for j in range(n):
        if a[i]>a[j] and i<j :
            count+=1
print(count)
"""
Output:
5
2 4 1  3 5
3
"""
