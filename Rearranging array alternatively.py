#Given a sorted array of positive integers. Your task is to rearrange  the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on.

n=int(input())
arr=[int(x) for x in input().strip().split(" ")]
temp = n*[None]
small, large = 0, n-1
flag = True
flag = True
for i in range(n):
        if flag is True:
            temp[i] = arr[large]
            large -= 1
        else:
            temp[i] = arr[small]
            small += 1
 
        flag = bool(1-flag)

for i in range(n):
        arr[i] = temp[i]
print(*arr)

"""
Output:
4
1 2 3 4
4 1 3 2
"""
