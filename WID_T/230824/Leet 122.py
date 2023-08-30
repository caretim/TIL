prices = [7,1,5,3,6,4]

start = len(prices)-1


result = 0
max_value = prices[start]
max_profit =0
temp_profit = 0
for i in range(start,-1,-1):
    if prices[i] < max_value:
        if max_value - prices[i] > max_profit:
            max_profit = max_value- prices[i]
    elif prices[i] > max_value:
        result+=max_profit
        max_profit=0
        max_value= prices[i]

result+= max_profit

print(result)



