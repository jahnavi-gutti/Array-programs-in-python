#Largest Number formed from an Array 
import functools
def compare(a,b):
    ab = int(str(a)+str(b))
    ba = int(str(b)+str(a))
    return ba-ab
    
def largestNumber(A):
    sorted_a = sorted(A,key=functools.cmp_to_key(compare))
    return int("".join([str(i) for i in sorted_a]))

t = int(input())

for i in range(0,t):
    n = int(input())
    arr = [int(x) for x in input().strip().split(" ")]
    print(largestNumber(arr))
"""
Output:
2
5
3
30 34
5 9
4
54 546 548
o/p
9534330
6054854654
"""
