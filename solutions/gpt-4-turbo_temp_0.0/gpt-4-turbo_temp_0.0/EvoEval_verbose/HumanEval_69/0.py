
def search(lst):
    frequency = {}
    for number in lst:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    greatest_integer = -1
    for (number, freq) in frequency.items():
        if number <= freq:
            greatest_integer = max(greatest_integer, number)
    return greatest_integer