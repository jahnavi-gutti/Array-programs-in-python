#Given a string S consisting only '0's and '1's,  find the last index of the '1' present in it.
n=int(input())
str =input()
x = '1'
index = -1
for i in range(0, len(str)):
	if str[i] == x:
		index = i
if index == -1:
	print("Character not found")
else:
	print(index)

"""
Output:
7
0010010
5
"""
