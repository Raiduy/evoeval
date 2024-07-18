def is_palindrome_sentence(sentence: str):
    cleaned_sentence = re.sub('\\W+', '', sentence).lower()
    return cleaned_sentence == cleaned_sentence[::-1]