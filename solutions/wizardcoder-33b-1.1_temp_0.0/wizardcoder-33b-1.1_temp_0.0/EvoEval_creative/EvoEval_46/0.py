def hidden_message(test_cases):
    secret_messages = []
    for test_case in test_cases:
        secret_message = ''.join((word[0] for word in test_case))
        if secret_message.isalpha():
            secret_messages.append(secret_message.lower())
        else:
            secret_messages.append('Take the cannoli.')
    return secret_messages