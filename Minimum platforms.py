x=int(input())
arrival = [int(i) for i in input().strip().split(" ")]
departure =[ int(i) for i in input().strip().split(" ")]
arrival.sort()
departure.sort()
count = 0
platforms = 0
i = j = 0
while i < len(arrival):
    if arrival[i] < departure[j]:
        count = count + 1
        platforms = max(platforms, count)
        i = i + 1
    else:
        count = count - 1
        j = j + 1

print("The minimum platforms needed is", platforms)
"""
Output:
09  6
90  0900 0940 0950 1100 1500 1800
0910 1200 1130 1900200              1120 1139 0 19001  2000
The minimum platforms needed is 3
"""
