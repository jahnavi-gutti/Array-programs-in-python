n=int(input())
price=list(map(int, input().strip().split(" ")))

if (n == 1):
	print(" ")
i=0
while (i < (n - 1)):
	while ((i < (n - 1)) and
			(price[i + 1] <= price[i])):
		i += 1
	if (i == n - 1):
		break
	buy = i
	i += 1
	while ((i < n) and (price[i] >= price[i - 1])):
		i += 1
	sell = i - 1
	print("Buy on day: ",buy,"\t",
"""				"Sell on day: ",sell)
Output:
7
100 180 260 310 40 535 695
Buy on day:  0 	 Sell on day:  3
Buy on day:  4 	 Sell on day:  6
"""
