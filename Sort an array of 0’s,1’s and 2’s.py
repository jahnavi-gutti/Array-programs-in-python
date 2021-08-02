#Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
n=int(input())
a=[int(x) for x in input().strip().split(" ")]
print(sorted(a))
"""
Output:
5
0 2 1 2  0
[0, 0, 1, 2, 2]
"""
