def palindromic_and_odd_digit_array(arr):

    def is_all_odd(num):
        """Check if all digits of num are odd."""
        return all((int(digit) % 2 != 0 for digit in str(num)))

    def min_changes_to_odd(num):
        """Determine the minimum changes to make num have all odd digits."""
        if is_all_odd(num):
            return 0
        digits = [int(digit) for digit in str(num)]
        for (i, digit) in enumerate(digits):
            if digit % 2 == 0:
                digits[i] = digit - 1 if digit > 0 else 1
        return 1
    changes = 0
    (left, right) = (0, len(arr) - 1)
    while left <= right:
        if arr[left] != arr[right]:
            changes += 1
            if not is_all_odd(arr[left]) and (not is_all_odd(arr[right])):
                changes += min(min_changes_to_odd(arr[left]), min_changes_to_odd(arr[right]))
            elif not is_all_odd(arr[left]):
                changes += min_changes_to_odd(arr[left])
            elif not is_all_odd(arr[right]):
                changes += min_changes_to_odd(arr[right])
        else:
            changes += min_changes_to_odd(arr[left])
        left += 1
        right -= 1
    return changes