def find_fruitful_days(prices, days):
    max_profit = 0
    min_price = prices[0]
    for i in range(days):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit