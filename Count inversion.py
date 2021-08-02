"""Given an array of integers. Find the Inversion Count in the array. 
Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
"""
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
