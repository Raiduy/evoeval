
def tri(n):
    sequence = [3]  # Initialize the sequence with the first element, which is always 3
    if n == 0:
        return sequence  # Return the sequence with only the first element if n is 0

    a, b, c = 1, 1, 3  # Initialize the variables for the Tribonacci sequence
    for i in range(1, n):
        if i % 2 == 0:
            next_num = 1 + i // 2  # Calculate the next number if i is even
        else:
            next_num = a + b + c  # Calculate the next number if i is odd
            a, b, c = b, c, next_num  # Update the variables for the Tribonacci sequence

        sequence.append(next_num)  # Add the next number to the sequence

    return sequence
