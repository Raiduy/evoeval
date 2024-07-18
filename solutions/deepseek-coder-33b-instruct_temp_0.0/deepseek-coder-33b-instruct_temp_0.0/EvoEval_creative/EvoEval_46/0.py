def hidden_message(test_cases):
    result = []
    for test_case in test_cases:
        secret_message = ''.join((word[0] for word in test_case))
        if secret_message.isalpha():
            result.append(secret_message.lower())
        else:
            result.append('Take the cannoli.')
    return result