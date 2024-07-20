def find_fruitful_days(prices, days):
    max_profit = 0
    for i in range(days):
        for j in range(i + 1, days):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
    return max_profit