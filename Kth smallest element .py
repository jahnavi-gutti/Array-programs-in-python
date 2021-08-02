#Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.
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
