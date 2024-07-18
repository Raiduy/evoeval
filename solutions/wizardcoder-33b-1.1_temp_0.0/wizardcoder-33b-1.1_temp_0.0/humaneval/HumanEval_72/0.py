
def will_it_fly(q, w):
    # Check if the list is a palindrome
    is_palindrome = q == q[::-1]

    # Check if the sum of the elements is less than or equal to w
    sum_less_than_w = sum(q) <= w

    # Return True if both conditions are met, False otherwise
    return is_palindrome and sum_less_than_w
