def translate_emoticons(sentence):
    """Convert text-based emoticons in a string to their corresponding Unicode emojis and return the result as a string.

    If the sentence doesn't contain any text-based emoticons, return the original sentence.
    Some examples of text-based emoticons and their corresponding emojis are ":)" corresponds to "😊", 
    ":(" corresponds to "☹️", ":D" corresponds to "😀", ";)" corresponds to "😉". 
    
    Examples:
    >>> translate_emoticons("Hello :) Have a nice day Marcus, how are you? :D")
    "Hello 😊 Have a nice day Marcus, how are you? 😀"
    >>> translate_emoticons("Oh no, it's raining Marcus, how is the weather? :(")
    "Oh no, it's raining Marcus, how is the weather? ☹️"
    >>> translate_emoticons("No emoticons here Marcus")
    "No emoticons here Marcus"
    """
    emoticons_to_emojis = {':)': '😊', ':(': '☹️', ':D': '😀', ';)': '😉'}
    words = sentence.split()
    for i in range(len(words)):
        if words[i] in emoticons_to_emojis:
            words[i] = emoticons_to_emojis[words[i]]
    return ' '.join(words)