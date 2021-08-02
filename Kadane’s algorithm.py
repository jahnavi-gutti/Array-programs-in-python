#Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
t = int(input())
for i in range(0,t):
    n = int(input())
    arr = [int(x) for x in input().strip().split(" ")]
    _sum = -1000
    max_sum = -1000;
    for item in arr:
        _sum = max(_sum,0) + item
        if _sum > max_sum:
            max_sum = _sum
    print( max_sum ) 
"""
Output:
5 1
5
1 2 3 -2 5
9
"""

