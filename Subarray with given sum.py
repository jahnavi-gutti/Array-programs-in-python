#Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

 
def subarray_with_given_sum(arr,n,s):
    start = 0
    current_sum = 0
    for i in range(0,n):
        current_sum = current_sum + arr[i]
        while(current_sum > s):
            current_sum = current_sum -arr[start]
            start = start + 1
        if current_sum == s:
            print(start+1,i+1)
            return
    print(-1) 
    return

t = int(input())

for i in range(0,t):
    n,s=map(int,input().split())

    arr = [int(x) for x in input().strip().split(" ")]
    subarray_with_given_sum(arr,n,s)
"""
Output:
2
5 12
1 2 3 7 5
2 4
10 15 
1 2 3 4 5 6 7 8 9 10
1 5
"""
