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
