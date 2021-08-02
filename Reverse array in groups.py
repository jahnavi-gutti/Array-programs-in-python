n=int(input())
k=int(input())
a = [int(i) for i in input().strip().split(" ")]
print(*a[k-1::-1],end=" ")
print(*a[:k-1:-1]
"""
Output:
5
3
1 2 3 4 5
3 2 1 5 4
"""
