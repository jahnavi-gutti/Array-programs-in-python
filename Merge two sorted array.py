#Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order without using any extra space. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.
 
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
