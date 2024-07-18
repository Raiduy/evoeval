def hidden_message(test_cases):
    secret_messages = []
    for test_case in test_cases:
        secret_message = ''
        for word in test_case:
            first_letter = re.search('[a-zA-Z]', word)
            if first_letter:
                secret_message += first_letter.group().lower()
        original_strings = ' '.join(test_case).lower()
        if secret_message in original_strings:
            secret_messages.append('Take the cannoli.')
        else:
            secret_messages.append(secret_message)
    return secret_messages