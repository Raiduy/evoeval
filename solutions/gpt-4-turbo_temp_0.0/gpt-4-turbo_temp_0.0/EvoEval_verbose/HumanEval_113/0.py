
def odd_count(lst):
    result = []
    for s in lst:
        odd_digits_count = sum((1 for char in s if int(char) % 2 != 0))
        formatted_message = 'the number of odd elements in the string of the input.'.replace('i', str(odd_digits_count))
        result.append(formatted_message)
    return result