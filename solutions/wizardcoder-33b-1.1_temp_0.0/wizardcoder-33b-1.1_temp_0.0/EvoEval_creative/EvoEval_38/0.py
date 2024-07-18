def translate_emoticons(sentence):
    emoticons = {':)': '😊', ':(': '☹️', ':D': '😀', ';)': '😉'}
    words = sentence.split()
    for i in range(len(words)):
        if words[i] in emoticons:
            words[i] = emoticons[words[i]]
    return ' '.join(words)