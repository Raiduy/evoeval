def translate_emoticons(sentence):
    """Convert text-based emoticons in a string to their corresponding Unicode emojis and return the result as a string.

    If the sentence doesn't contain any text-based emoticons, return the original sentence.
    Some examples of text-based emoticons and their corresponding emojis are ":)" corresponds to "😊", 
    ":(" corresponds to "☹️", ":D" corresponds to "😀", ";)" corresponds to "😉". 
    
    Examples:
    >>> translate_emoticons("Hello :) Have a nice day! :D")
    "Hello 😊 Have a nice day! 😀"
    >>> translate_emoticons("Oh no, it's raining! :(")
    "Oh no, it's raining! ☹️"
    >>> translate_emoticons("No emoticons here")
    "No emoticons here"
    """
    emoticons = {':)': '😊', ':(': '☹️', ':D': '😀', ';)': '😉'}
    for (emoticon, emoji) in emoticons.items():
        sentence = sentence.replace(emoticon, emoji)
    return sentence