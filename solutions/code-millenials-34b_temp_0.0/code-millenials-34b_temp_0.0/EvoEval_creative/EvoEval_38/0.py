def translate_emoticons(sentence):
    emoticons = {':)': '😊', ':(': '☹️', ':D': '😀', ';)': '😉'}
    for (emoticon, unicode_emoji) in emoticons.items():
        sentence = sentence.replace(emoticon, unicode_emoji)
    return sentence