t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip(" ").split(" ")]
        
    if len(arr) == 0:
        print(-1)
    left_max = arr[0]
    left = []
    for i in range(1,n-1):
        if arr[i]>=left_max:
            left.append(i)
            left_max = arr[i]
    
    right_min = arr[n-1]
    right = []
    for i in range(1,n-1):
        if arr[n-1-i] <= right_min:
            right.append(n-1-i)
            right_min = arr[n-1-i]
    
    for i in left:
        if i in right:
            print(arr[i])
    else:
        print(-1)
"""
Output:
2
4
4 5   2 5 7
5
3
11 9 12
-1
"""
