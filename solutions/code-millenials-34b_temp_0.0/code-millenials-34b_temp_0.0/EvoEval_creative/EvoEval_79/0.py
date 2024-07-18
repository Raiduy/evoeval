def find_fruitful_days(prices, days):
    max_profit = 0
    min_price = prices[0]
    for i in range(1, days):
        if prices[i] > min_price:
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        else:
            min_price = prices[i]
    return max_profit