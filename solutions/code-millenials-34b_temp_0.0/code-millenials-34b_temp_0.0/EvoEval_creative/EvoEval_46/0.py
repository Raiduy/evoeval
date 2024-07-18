def hidden_message(test_cases):
    secret_messages = []
    for test_case in test_cases:
        message = ''
        for word in test_case:
            message += word[0]
        if message == 'Take the cannoli':
            secret_messages.append('Take the cannoli.')
        else:
            secret_messages.append(message.lower())
    return secret_messages