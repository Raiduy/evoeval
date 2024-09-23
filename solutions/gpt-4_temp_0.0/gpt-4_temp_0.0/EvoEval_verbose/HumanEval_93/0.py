
def encode(message):
    """
    This function is designed to perform a specific encoding task on a given message. The encoding rules are as follows:
    
    1. All letters in the message are to be swapped for their case counterparts. In other words, all lowercase letters 
    become uppercase and all uppercase letters become lowercase.

    2. All vowels in the message are to be replaced with the letter that is exactly two places ahead of them in the 
    English alphabet. For example, 'a' would be replaced with 'c', 'e' would be replaced with 'g', and so on. 

    The function assumes that the input will only contain letters. No numbers, punctuation marks, or special characters 
    will be included in the input message.

    To illustrate how this function works, let's look at some examples:

    If the input message is 'test', the function will return 'TGST'. The 'e' in 'test' is replaced by 'g' (since 'g' 
    is two places ahead of 'e' in the English alphabet). All other letters are simply swapped for their case counterparts.

    If the input message is 'This is a message', the function will return 'tHKS KS C MGSSCGG'. The 'i' in 'This' is 
    replaced by 'k' (since 'k' is two places ahead of 'i' in the English alphabet), 'a' in 'a' is replaced by 'c' 
    (since 'c' is two places ahead of 'a' in the English alphabet), and the 'e' in 'message' is replaced by 'g' 
    (since 'g' is two places ahead of 'e' in the English alphabet). All other letters are simply swapped for their case 
    counterparts.
    """
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char in vowels:
            if char.isupper():
                encoded_message += chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
            else:
                encoded_message += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        else:
            encoded_message += char.swapcase()
    return encoded_message