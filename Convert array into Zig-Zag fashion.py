#Given an array Arr (distinct elements) of size N. Rearrange the elements of array in zig-zag fashion. The converted array should be in form a < b > c < d > e < f. The relative order of elements is same in the output i.e you have to iterate on the original array only
n=int(input())
a= [int(x) for x in input().strip(" ").split(" ")]
f=True
for i in range(n-1): 
    if f is True: 
        print(a[i],"<",end=" ")
        f = bool(1 - f) 
    else: 
         print(a[i],">",end=" ")
print(a[-1])
"""
Output:
7
4 3 7 8 6 2 1
4 < 3 > 7 > 8 > 6 > 2 > 1
"""
