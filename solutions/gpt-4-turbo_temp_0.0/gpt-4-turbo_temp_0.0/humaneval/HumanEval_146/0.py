
def specialFilter(nums):
    def isOdd(n):
        """Check if a number is odd."""
        return n % 2 != 0

    def meetsCriteria(n):
        """Check if the number is greater than 10, and both the first and last digits are odd."""
        if n <= 10:
            return False
        str_n = str(abs(n))  # Convert to string and remove sign if negative
        first_digit = int(str_n[0])
        last_digit = int(str_n[-1])
        return isOdd(first_digit) and isOdd(last_digit)

    # Use a list comprehension to filter numbers that meet the criteria and return their count
    return sum(1 for num in nums if meetsCriteria(num))
