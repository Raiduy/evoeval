
def exchange(lst1, lst2):
    # Check if all elements in lst1 are even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Check if there is at least one odd number in lst1 and at least one even number in lst2
    if any(num % 2 != 0 for num in lst1) and any(num % 2 == 0 for num in lst2):
        return "YES"

    return "NO"
