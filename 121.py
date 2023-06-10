left = 0
right = 1
MaxProfit = 0

while right < len(prices):
    # profit
    if prices[left] < prices[right]:
        profit = prices[right] - prices[left]
        MaxProfit = max(profit, MaxProfit)
    else:
        left = right
    right+=1
    
return MaxProfit