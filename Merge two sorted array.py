n=int(input())
a=[int(x) for x in input().strip().split(" ")]
m=int(input())
b=[int(x) for x in input().strip().split(" ")]
k=a+b
l=sorted(k)
print(l[0:n])
print(l[n:])

"""
Output:
4
1 3 5 7
3
2 4 6
[1, 2, 3, 4]
[5, 6, 7]
"""
