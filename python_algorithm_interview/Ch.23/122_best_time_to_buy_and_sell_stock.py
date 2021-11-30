prices = [7,1,5,3,6,4]
res = 0
for i in range(len(prices)):
    if prices[i] < prices[i+1]:
        res += prices[i+1]-prices[i]
    