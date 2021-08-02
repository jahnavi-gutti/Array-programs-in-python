#Given two arrays X and Y of positive integers, find the number of pairs such that xy > yx (raised to power of) where x is an element from X and y is an element from Y.
m=int(input())
a=[int(x) for x in input().strip().split(" ")]
n=int(input())
b=[int(x) for x in input().strip().split(" ")]
count=0
for i in a:
    for j in b:
        if i**j>j**i:
            count+=1
print(count)
"""
Output:
4
2 3 4 5
3
1 2 3
5
"""
