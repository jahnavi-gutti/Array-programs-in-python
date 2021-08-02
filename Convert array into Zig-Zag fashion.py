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
