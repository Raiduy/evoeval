def hidden_message(test_cases):
    secret_messages = []
    for test_case in test_cases:
        secret_message = ''
        for word in test_case:
            secret_message += word[0]
        if 'cannoli' in secret_message.lower():
            secret_message = 'Take the cannoli.'
        secret_messages.append(secret_message.lower())
    return secret_messages