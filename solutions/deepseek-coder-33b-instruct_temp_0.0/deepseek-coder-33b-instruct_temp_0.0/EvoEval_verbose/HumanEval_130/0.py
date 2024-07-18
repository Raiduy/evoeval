
def tri(n):
    """
    The Fibonacci sequence is a well-known number sequence that has been extensively studied by mathematicians over the past centuries. However, a less commonly known sequence is the Tribonacci sequence.

    The Tribonacci sequence is a sequence of numbers defined by a specific set of recurrence relations. The sequence begins with the number 3 (when n equals to 1), and the subsequent numbers in the sequence are defined as follows:

    For an even number 'n', the nth element of the Tribonacci sequence, tri(n), is calculated as 1 plus n divided by 2.

    For an odd number 'n', the nth element of the Tribonacci sequence, tri(n), is calculated as the sum of the previous number in the sequence (tri(n - 1)), the number two places before it (tri(n - 2)), and the number after it (tri(n + 1)).

    As an example, tri(2), where n is even, would be calculated as 1 + (2 / 2) to give a result of 2. tri(4) would be calculated as 1 + (4 / 2) to give a result of 3. tri(3), where n is odd, would be calculated as the sum of tri(2), tri(1), and tri(4) to give a result of 8.

    The task at hand is to write a function that takes a non-negative integer 'n' as input and returns a list of the first 'n' + 1 numbers in the Tribonacci sequence.

    Example:
    Given an input of 3, the function should return a list of the first 4 numbers in the Tribonacci sequence: [1, 3, 2, 8]

    :param n: Non-negative integer indicating the number of elements from the Tribonacci sequence to generate.
    :return: A list of the first 'n' + 1 numbers from the Tribonacci sequence.
    """
    tribonacci = [1, 3, 2]
    for i in range(3, n + 1):
        if i % 2 == 0:
            tribonacci.append(1 + i / 2)
        else:
            tribonacci.append(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3])
    return tribonacci