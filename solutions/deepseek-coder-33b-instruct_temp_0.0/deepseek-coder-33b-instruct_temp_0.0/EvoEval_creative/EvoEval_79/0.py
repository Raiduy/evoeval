def find_fruitful_days(prices, days):
    """
    Given a list of prices of a certain fruit and the number of days a vendor has stayed in the market, 
    find the maximum profit that could be made by the vendor if he could buy and sell the fruit only once during his stay.

    The vendor has the ability to know the prices of the fruit in the future. 
    He wants to buy the fruit on one day and sell it on another day that comes after the day he bought the fruit.
    If he cannot make any profit, return 0.

    Args:
        prices (list): A list of integers representing the prices of the fruit for each day.
        days (int): The latest of day the vendor can buy fruits.

    Returns:
        int: The maximum profit that could be made by the vendor.

    Example:

        Input: prices = [1, 5, 2, 8, 7, 3], days = 5
        Output: 7 # The vendor buys the fruit on the first day at price 1 and sells it on the fourth day at price 8.

    Constraints:
        1. 1 <= len(prices) <= 100
        2. 1 <= days <= len(prices)
    """
    max_profit = 0
    min_price = prices[0]
    for i in range(1, days):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit