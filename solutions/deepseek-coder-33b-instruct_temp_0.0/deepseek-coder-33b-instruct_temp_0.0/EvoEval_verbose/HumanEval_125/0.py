
def split_words(txt):
    """
    This function named 'split_words' takes in a single parameter:
    - txt (a string): This parameter represents a string of words that could be separated by whitespace or commas or contains a mix of lowercase and uppercase letters.

    The function works in the following way:

    - Firstly, the function checks for the presence of whitespaces in the given string. If the string contains whitespaces, the function splits the string on these whitespaces and returns a list of words.

    - If the string does not contain any whitespace, the function then checks for the presence of commas. If commas are present, the function splits the string on these commas and returns a list of words.

    - If neither whitespaces nor commas are present in the string, the function then counts the number of lowercase letters that have an odd order in the alphabet. Here, the order is determined by subtracting the unicode value of 'a' from the unicode value of the letter, thus 'a' has an order of 0, 'b' has an order of 1 and so on till 'z' which has an order of 25.

    The aim of the function is to return a list of words in the given string, split based on specific separators (whitespaces or commas). If no such separators are present, the function returns a count of lowercase letters with an odd order.

    Examples:
    - If the function is called with the string "Hello world!" like so: split_words("Hello world!"), the function would return ["Hello", "world!"]

    - If the function is called with the string "Hello,world!" like so: split_words("Hello,world!"), the function would return ["Hello", "world!"]

    - If the function is called with the string "abcdef" like so: split_words("abcdef"), the function would return 3 as 'b', 'd' and 'f' are the lowercase letters with an odd order in the alphabet.
    """
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum((1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 != 0))