def translate_emoticons(sentence):
    emoticons = {':)': '😊', ':(': '☹️', ':D': '😀', ';)': '😉'}
    for (emoticon, emoji) in emoticons.items():
        sentence = sentence.replace(emoticon, emoji)
    return sentence