def hidden_message(test_cases):
    """
    Covert Agent X has a unique way of encrypting secret messages for others 
    to decipher. He encrypts his messages by providing strings of words, where 
    the first letter of each word (when pieced together) forms a secret message.

    Your task is to write a function that takes in a group of test cases, 
    and returns the secret message from each test case.

    Each test case is a list of strings. The function should return a list of strings,
    where each string is a secret message decoded from a test case.
    If the secret message can be found within the original strings, the secret message is now "Take the cannoli."

    Note: 
    - Words may have symbols next to them, but these should be ignored.
    - Return the message in lowercase

    Examples:
    hidden_message([['Hello, world!', 'okay?'], ['Every', 'good', 'boy', 'does', 'fine']]) -> ['ho', 'egbdf']
    hidden_message([['apple'], ['Banana', 'grape', 'kiwi', 'melon']]) -> ['Take the cannoli.', 'bgkm']
    hidden_message([['This', 'is', '?a', 'test', 'case??'], ['hi']]) -> ['tiatc', 'Take the cannoli.']
    """
    result = []
    for test_case in test_cases:
        message = ''
        for string in test_case:
            words = string.split()
            for word in words:
                message += word[0].lower()
        if message in ' '.join(test_case).lower():
            message = 'Take the cannoli.'
        result.append(message)
    return result