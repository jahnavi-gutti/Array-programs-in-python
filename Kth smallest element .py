n=int(input())
k=int(input())
a = [int(i) for i in input().strip().split(" ")]
b=sorted(a)
print(b[k-1])
"""
Output:
6
3
7 10 4 3 20 15
7
"""
