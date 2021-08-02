#Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are M students, the task is to distribute chocolate packets among M students such that :
#1. Each student gets exactly one packet.
#2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.
n=int(input())
m=int(input())
a=list(map(int, input().strip().split(" ")))
b=sorted(a)
min=b[-1]
for i in range(n-m):
    dif=b[i+m-1]-b[i]
    if(dif<min):
        min=dif
print(min)
"""
Output:


8
5
3 4 1 9 56 7 9 12
6
"""
