#Given a matrix of size r*c. Traverse the matrix in spiral form.
m = int(input())
n = int(input())
arr = []
# initialize the number of rows
for i in range(0,m):
    arr += [0]
# initialize the matrix
for i in range (0,m):
    arr[i] = [0]*n
for i in range (0,m):
    for j in range (0,n):
        arr[i][j] = int(input())
print ("\nThe Matrix is")
for i in range (0,m):
    for j in range (0,n):
        print(arr[i][j], end = " ")
    print("\n")
k = 0; l = 0
print("Spiral Matrix : ",end = " ")
while (k < m and l < n):
    for i in range(l, n):
        print(arr[k][i], end = " ")
    k += 1
    for i in range(k, m):    
        print(arr[i][n-1], end = " ")
    n -= 1
    if ( k < m):
        for i in range(n-1, (l - 1), -1) :
            print(arr[m-1][i], end =" ")  
            m -= 1
    if (l < n):
        for i in range(m - 1, k - 1, -1):
            print(arr[i][l], end =" ")
        l += 1
"""
Output:
3 
6
12 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
1 2 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
"""
