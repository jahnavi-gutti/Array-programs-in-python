#Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
#Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.

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
